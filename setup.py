from setuptools import setup, find_packages

setup(
    name='shetue_custom_app', # <--- পরিবর্তন করুন
    version='0.0.1',
    description='Customizations for Shetue MultiBiz ERPNext',
    author='Sohel Huq',
    packages=['shetue_custom_app'], # <--- পরিবর্তন করুন
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
)
