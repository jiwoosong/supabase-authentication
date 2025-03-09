import importlib.util
import sys
import os

# 🔹 운영체제별 확장자 설정
ext = ".pyd" if sys.platform == "win32" else ".so"

# 🔹 `.so` 또는 `.pyd` 파일이 존재하는지 확인 후 import
client_path = os.path.join(os.path.dirname(__file__), f"client{ext}")
admin_path = os.path.join(os.path.dirname(__file__), f"admin{ext}")

if os.path.exists(client_path):
    spec = importlib.util.spec_from_file_location("supabase_auth.client", client_path)
    client = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(client)
    sys.modules["supabase_auth.client"] = client

if os.path.exists(admin_path):
    spec = importlib.util.spec_from_file_location("supabase_auth.admin", admin_path)
    admin = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(admin)
    sys.modules["supabase_auth.admin"] = admin

import supabase_auth.client
import supabase_auth.admin