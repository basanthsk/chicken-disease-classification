with open("README.md","r",encoding="utf-8") as f:
    log_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "chicken-disease-classification"
AUTHOR_USER_NAME = "Basanth"
SRC_REPO = "chickenClassifier"
AUTHOR_EMAIL = "basanthsk@gmail.com" 


setuptools.setup(
    name = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A pythn package for chicken disease calssification",
    long_description =log_description,
    log_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where="src")
    
)   