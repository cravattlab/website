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

```

```


## Updating hugo binaries

From the root folder of this repository, issue the following command:

```bash
./scripts/get-latest-hugo.sh
```


## If ever we want to abandon hugo

