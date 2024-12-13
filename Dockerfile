FROM public.ecr.aws/lambda/python@sha256:4835868c64d5be2b2196850ae892a6c40899a63bb9d0e87073aa21cc8654d8a9 AS build
RUN dnf install -y unzip && \
    curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.69/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.69/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /tmp/ && \
    unzip /tmp/chrome-linux64.zip -d /tmp/

FROM public.ecr.aws/lambda/python@sha256:4835868c64d5be2b2196850ae892a6c40899a63bb9d0e87073aa21cc8654d8a9

COPY pyproject.toml run.py entrypoint.sh requirements.txt ${LAMBDA_TASK_ROOT}/
COPY src/ ${LAMBDA_TASK_ROOT}/src/

RUN chmod +x ${LAMBDA_TASK_ROOT}/entrypoint.sh

ENV DISPLAY=:99

RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm \
    xorg-x11-utils
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=build /tmp/chrome-linux64 /tmp/chrome
COPY --from=build /tmp/chromedriver-linux64 /tmp/chromedriver


CMD [ "src.tracklist1001.handler" ]

ENTRYPOINT [ "/var/task/entrypoint.sh" ]


