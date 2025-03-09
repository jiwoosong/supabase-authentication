from setuptools import setup, Extension
from Cython.Build import cythonize
import platform

version = '0.0.1'
install_requires = ["requests"]
ext = ".pyd" if platform.system() == "Windows" else ".so"

ext_modules = [
    Extension("supabase_auth.client", ["supabase_auth/client.py"]),
    Extension("supabase_auth.admin", ["supabase_auth/admin.py"])
]

setup(
    name='supabase_auth',
    author='Jiwoo Song',
    author_email='sjw0297@iheuron.com',
    version=version,
    packages=["supabase_auth"],  # 🔹 패키지 포함
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level': "3"}),
    include_package_data=True,  # 🔹 바이너리 파일 포함
    description='Custom Authentication Tool',
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "supabase-client = supabase_auth.client:manage_license",
            "supabase-admin = supabase_auth.admin:admin_interface"
        ]
    },
)