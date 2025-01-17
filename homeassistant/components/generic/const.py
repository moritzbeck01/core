"""Constants for the generic (IP Camera) integration."""

DOMAIN = "generic"
DEFAULT_NAME = "Generic Camera"
CONF_CONTENT_TYPE = "content_type"
CONF_LIMIT_REFETCH_TO_URL_CHANGE = "limit_refetch_to_url_change"
CONF_STILL_IMAGE_URL = "still_image_url"
CONF_STREAM_SOURCE = "stream_source"
CONF_FRAMERATE = "framerate"
CONF_RTSP_TRANSPORT = "rtsp_transport"
CONF_USE_WALLCLOCK_AS_TIMESTAMPS = "use_wallclock_as_timestamps"
FFMPEG_OPTION_MAP = {
    CONF_RTSP_TRANSPORT: "rtsp_transport",
    CONF_USE_WALLCLOCK_AS_TIMESTAMPS: "use_wallclock_as_timestamps",
}
RTSP_TRANSPORTS = {
    "tcp": "TCP",
    "udp": "UDP",
    "udp_multicast": "UDP Multicast",
    "http": "HTTP",
}
GET_IMAGE_TIMEOUT = 10

DEFAULT_USERNAME = None
DEFAULT_PASSWORD = None
DEFAULT_IMAGE_URL = None
DEFAULT_STREAM_SOURCE = None
