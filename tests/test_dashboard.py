import os

def test_files_exist():
    assert os.path.exists("dashboard.py")
    assert os.path.exists("modules/network_scanner.py")
    assert os.path.exists("modules/tool_manager.py")
    assert os.path.exists("modules/privacy_mode.py")