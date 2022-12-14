from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.web.server.browser_websocket_handler import BrowserWebSocketHandler

import streamlit as st
from streamlit import runtime


def is_running_on_cloud() -> bool:
    """Return True if the app is running on Community Cloud. Defaults to False.
    Raise an error if the server is not running.
    Note to the intrepid: this is an UNSUPPORTED, INTERNAL API. (We don't have plans
    to remove it without a replacement, but we don't consider this a production-ready
    function, and its signature may change without a deprecation warning.)
    """
    ctx = get_script_run_ctx()
    if ctx is None:
        return None

    session_client = runtime.get_instance().get_client(ctx.session_id)
    if session_client is None:
        return None

    if not isinstance(session_client, BrowserWebSocketHandler):
        raise RuntimeError(
            f"SessionClient is not a BrowserWebSocketHandler! ({session_client})"
        )
    hostname = dict(session_client.request.headers)["Host"]

    if hostname.endswith("streamlit.app"):
        return True
    return False


st.write("App running on Community Cloud?", is_running_on_cloud())

