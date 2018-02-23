# Cravatt Lab Website v2.0

If you're an alumni, or current member and would like your information to be changed, please feel free to submit an issue or pull request.

The `v2.0` refers to the fact that the website is now built using the static site generator [hugo](https://gohugo.io/). While the template is the same as before, this allows us to modify and add new lab members/alumni without having to edit HTML markup directly. Eventually this can be extended to references, and the research page. It would also be very easy to offer individual research pages for every lab members, although at time of writing this is disabled.


## Adding new lab members

To add a new lab member, go the `src/content/members` directory and create a file with the name `LASTNAME.FIRSTNAME.md`. The naming convention is important for sorting lab members by last name. Make sure that you are using the `.md` extension, otherwise `hugo` will fail to process the files.

The contents of the file should follow this format. The `---` at the start and end identify this as a header. If we were to have additional content for each lab member (ie. description of individual projects), that information would go below the bottom `---`.

```
---
name: NAME_HERE, Ph.D.
position: POSITION_HERE
honorifics:
    - FELLOWSHIP_TITLE_HERE
    - ADDITIONAL_FELLOWSHIP
telephone: (858) 784-8636
email: EMAIL HERE
picture: example.jpg
---
```

The following sections are optional: honorifics, telephone, email, and picture. When defined, honorifics should follow the format above.


## Adding pictures for new lab members

Pictures should be uploaded in `src/static/images/people`.


## Adding alumni

This is very similar to adding new lab members. Go to `src/content/alumni` and create a file with the name `LASTNAME.FIRSTNAME.md`. The format is slightly different:

```
---
name: NAME_HERE, Ph.D.
position: POSITION_HERE
current_position:
    - Assistant Professor
    - New York, NY
email: bachovcd@mskcc.org
lab:
    url: COMPLETE_URL_TO_LAB_WEBSITE_HERE
    text: LINK_TEXT_FOR_THE_ABOVE
---
```

You may specify additional lines, for example to specify location, or additional position by adding new items underneath `current_position`. 


## Removing lab members or alumni

Simply delete the file in the appropriate directory. `src/content/members` for current members, and `src/content/alumni` for alumni.


## Building the site

For consistent invokation between Linux and macOS, hugo binaries for both platforms are stored in the `bin/` directory. `hugo.sh` acts as proxy and chooses the correct one depending on your platform. The website can also be built on windows with a `hugo.exe`, but this binary is not included in this repository.

To build, issue the following command from the main directory of this repository:

```bash
./hugo.sh
```


## Previewing changes

From the main directory of this repository issue the following command:

```bash
./hugo.sh serve
```

You will see a message similar to the following:

```bash
$ ./hugo.sh serve

                   | EN
+------------------+----+
  Pages            |  5
  Paginator pages  |  0
  Non-page files   |  0
  Static files     | 86
  Processed images |  0
  Aliases          |  0
  Sitemaps         |  0
  Cleaned          |  0

Total in 2901 ms
Watching for changes in /mnt/d/Documents/GitHub/website2/src/{content,layouts,static}
Serving pages from /mnt/d/Documents/GitHub/website2/build
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/cravatt/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Note that it tells you to go to `http://localhost:1313/cravatt/` in your browser to view the site.


## Updating hugo binaries

From the root folder of this repository, issue the following command:

```bash
./scripts/get-latest-hugo.sh
```


## Using git hooks to automate deployment

On the machine the website is hosted:

```
git config init.templatedir .git-templates
chmod a+x .git-templates/hooks/*
git init
```

Keep in mind that some of the hooks found in `.git-templates` are meant to be executed on a particular machine. For example there is a `post-merge` hook that when run on the scripps server, will rsync the contents of the latest build and update the website.


## If ever we want to abandon hugo

Simply build the site, and carry on with the `.html` files.
