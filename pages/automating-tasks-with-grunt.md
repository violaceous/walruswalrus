published: true
title: Automating tasks with Git hooks
date: 12-20-2013
tags: [Git, workflow, S3] 

I am currently hosting this blog on Amazon S3. To deploy updates and new posts I am using [s3cmd](s3tools.org/s3cmd) which allows you to perform tasks related to S3 from the command line. It was easy enough to setup; you run `s3cmd --configure` which asks you for some basic information needed to access your account such as your username and the access keys. I was a bit confused by the encryption key steps as I wasn't sure if this was something I was supposed to set up with amazon or not. I entered one of the handful of passwords I typically use and nothing broke so I will continue to ignore that option until something does break. 

I was stuck for a bit during my initial setup on how to specify the S3 bucket I wanted to deploy my files to. The mistake I was making was trying to use the endpoint Amazon had given when I setup the bucket. The easiest way to figure this out is to to use the `s3cmd ls` command which lists the buckets you have in your account. I then used `s3cmd sync build/ s3://walruswalr.us` to push my files where `build` is the directory my site has been built in and `s3://walruswalr.us` is my bucket. So far so good.

I hit a bit of a snag just now though. I had made some minor changes to the site and added in the ability to be able to add posts and have them not be published (as one of the 3 posts I went live with was half-written) as well as a few other minor enhancements but when I used `s3cmd sync` to push my changes to Amazon my deployed site didn't change. The first thing I found surprising was that it looked like s3cmd was pushing up every file again which doesn't scream "sync" to me. That should have clued me into what was wrong. I gave it some time as I think I have seen somewhere that S3 is eventually consistent and my favorite way to fix problems is have them magically fix themselves but it didn't work. The next thing I like to try is start with a clean slate (when it is easy to do so anyway) so I deleted everything in my bucket using `s3cmd del --recursive --force s3://walruswalr.us` and ran the sync command again. And after looking at the files that went up I realized my mistake - I left the trailing / off build so instead instead of entering the build directory and then syncing files it synced from the current location and put everything up in the build directory. If I had noticed this and gone to walruswalr.us/build/index.html I would have seen my new changes. 

I started looking into automating this using Grunt but it didn't seem quite right for the task at hand. I was googling around a bit to see how people make Grunt and Git work together when I ran across Git Hooks. I won't be (intentionally anyway) pushing any code to github that isn't ready for production so I would like an automated push to S3 to happen when I push code to git. All I need to do to make that happen is have the post-commit hook (there isn't a post-push hook so this is nearly as good) be:

`#!/bin/sh`

`python sitebuilder.py build`

`s3cmd sync build/ s3://walruswalr.us`

The first command builds the static version of the site and the second command syncs it with S3. I put it at the root of my project as post-commit.sh so it is tracked and added "Run `ln -s post-commit.sh .git/hooks/post-commit` to have the site automatically deploy to S3 when a commit is made." to the README.md so that I remember to install it in the future. And then I used it to send this very post right here up to amazon. One less thing for me to have to remember, which is good, because I can't remember much.







