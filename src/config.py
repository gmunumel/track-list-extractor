import posixpath


def get_tracklist_v1_url():
    return posixpath.join("/", "api", "v1", "tracklist")
