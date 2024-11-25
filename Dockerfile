FROM public.ecr.aws/lambda/python@sha256:4835868c64d5be2b2196850ae892a6c40899a63bb9d0e87073aa21cc8654d8a9 AS build
RUN dnf install -y unzip && \
    curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.69/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.69/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /opt/ && \
    unzip /tmp/chrome-linux64.zip -d /opt/

FROM public.ecr.aws/lambda/python@sha256:4835868c64d5be2b2196850ae892a6c40899a63bb9d0e87073aa21cc8654d8a9
COPY pyproject.toml run.py requirements.txt ${LAMBDA_TASK_ROOT}/
COPY src/ ${LAMBDA_TASK_ROOT}/src/

RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=build /opt/chrome-linux64 /opt/chrome
COPY --from=build /opt/chromedriver-linux64 /opt/chromedriver

CMD ["src.tracklist.handler"]
