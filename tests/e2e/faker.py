from src.domain.session import Session
from src.domain.track import Track


class Faker:
    @property
    def foo_session(self) -> Session:
        return Session(
            tracks=[
                Track(
                    id="id_1",
                    number="01",
                    time="00:00",
                    name="foo",
                    label="bar",
                ),
                Track(
                    id="id_2",
                    number="02",
                    time="05:00",
                    name="baz",
                    label="qux",
                ),
            ],
            source="foo_source",
            name="foo_name",
            total_tracks="2",
        )
