from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os
import platform

version = '0.0.1'
install_requires = ["requests"]

# 운영체제에 따라 확장자 설정
ext = ".pyd" if platform.system() == "Windows" else ".so"

# Cython으로 변환할 확장 모듈 정의
ext_modules = cythonize([
    Extension("supabase_auth.client", ["supabase_auth/client.py"]),
    Extension("supabase_auth.admin", ["supabase_auth/admin.py"])
], compiler_directives={'language_level': "3"})

setup(
    name='supabase_auth',
    version=version,
    author='Jiwoo Song',
    author_email='sjw0297@iheuron.com',
    description='Custom Authentication Tool',
    packages=find_packages(),  # 🔹 패키지 자동 탐색
    include_package_data=True,  # 🔹 바이너리 파일 포함
    ext_modules=ext_modules,  # 🔹 Cython 변환된 모듈 포함
    package_data={"supabase_auth": ["*.pyd", "*.so"]},  # 🔹 바이너리 파일 포함 설정
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "supabase-client = supabase_auth.client:manage_license",
            "supabase-admin = supabase_auth.admin:admin_interface"
        ]
    },
)

# 🔹 빌드 후 소스코드 삭제 (보안 강화)
for py_file in ["supabase_auth/client.py", "supabase_auth/admin.py"]:
    if os.path.exists(py_file):
        os.remove(py_file)
