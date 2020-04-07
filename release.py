
# Script to create release notes, binary, and upload all that to GitHub
# Work in progress

import platform
import os
import shutil
from git import Repo
import requests
import subprocess

DRY_RUN = False
repo = Repo(os.getcwd())
detached_tag = repo.git.describe('--tags')
if "-" not in detached_tag:
    print("No changes from the latest tag. Nothing to do.")
    exit(0)

if repo.active_branch.name != "master":
    print("This should only be run on the master branch.")
    exit(0)


def release_to_github(tag, platform, commits=[]):
    release = requests.post("https://api.github.com/repos/numbertheory/"
                            "dungeon-dos/releases",
                            auth=(os.getenv('GITHUB_TOKEN'), ''),
                            json={
                              "tag_name": tag,
                              "tag_commitish": "master",
                              "name": "Dungeon DOS - {}".format(tag),
                              "body": "\n".join(commits),
                              "draft": True,
                              "prerelease": True}).json()
    # Upload the asset
    zip_archive = "dungeon-dos-{}-{}.zip".format(platform, tag)
    zip_headers = {"Content-Type": "application/zip",
                   "Content-Length": "".format(os.path.getsize(
                                                 zip_archive))}
    upload_url = "{}?name={}".format(
                    release["upload_url"][:-13],
                    zip_archive)
    with open(zip_archive, 'rb') as zip_file:
        upload = requests.post(upload_url,
                               auth=(os.getenv('GITHUB_TOKEN'), ''),
                               headers=zip_headers,
                               data=zip_file)
    if upload.ok:
        print("Release Completed!")
        print("{}".format(next_tag))
        print("{}".format(release["html_url"]))
    else:
        print("Release Failed!")
        print(upload.text)


def increment_last_tag(last_tag, release_type="bugfix"):
    if release_type == "minor":
        next_tag = [int(last_tag.split('.')[0][1:]),
                    int(last_tag.split('.')[1]) + 1,
                    int(last_tag.split('.')[2])]
    elif release_type == "major":
        next_tag = [int(last_tag.split('.')[0][1:]) + 1,
                    int(last_tag.split('.')[1]),
                    int(last_tag.split('.')[2])]
    elif release_type == "bugfix":
        next_tag = [int(last_tag.split('.')[0][1:]),
                    int(last_tag.split('.')[1]),
                    int(last_tag.split('.')[2]) + 1]
    return "v{}".format(".".join([str(x) for x in next_tag]))


def cleanout_builds():
    try:
        shutil.rmtree('build/')
    except FileNotFoundError:  # noqa: F821
        pass

    try:
        shutil.rmtree('dist/')
    except FileNotFoundError:  # noqa: F821
        pass

    try:
        os.remove('dungeon-dos.spec')
    except FileNotFoundError:  # noqa: F821
        pass


if platform.system().lower() == "windows":
    print("Releasing for Windows.")
    print("Cleaning out old build directories.")
    cleanout_builds()

    all_tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    last_tag = str(all_tags[-1])
    next_tag = increment_last_tag(last_tag)
    print("Preparing release for: {}".format(next_tag))
    changed_files = [item.a_path for item in repo.index.diff(None)]
    if len(changed_files) != 0:
        # Don't release if there are uncommitted changes
        print("Commit changes to git history to proceed.")
        exit(2)

    repo.create_tag(next_tag)
    repo.remotes.origin.push(next_tag)

    # Build the tagged release for Windows
    windows_output = subprocess.Popen("release_win.bat",
                                      shell=True,
                                      stdout=subprocess.PIPE).stdout.read()
    print(windows_output.decode('utf-8'))
    zip_output = subprocess.Popen("7z a -tzip dungeon-dos-Windows10-{}.zip"
                                  " ./dist/scenes/ "
                                  " ./dist/dungeon-dos.exe".format(
                                    next_tag
                                  ),
                                  shell=True,
                                  stdout=subprocess.PIPE).stdout.read()
    print(zip_output.decode('utf-8'))

    # Draft a new release with the tag
    release_to_github(next_tag, "Windows10", commits=[])

elif platform.system().lower() == "linux":
    print("Releasing for Linux.")
    print("Cleaning out old build directories.")
    cleanout_builds()
    all_tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    last_tag = str(all_tags[-1])
    next_tag = increment_last_tag(last_tag)
    print("Preparing release for: {}".format(next_tag))
    changed_files = [item.a_path for item in repo.index.diff(None)]
    if len(changed_files) != 0:
        # Don't release if there are uncommitted changes
        print("Commit changes to git history to proceed.")
        exit(2)
