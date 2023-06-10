[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<br />


<p>
  <a href="https://github.com/jerlendds/osintbuddy">
    <img src="./docs/watermark.svg" height="130px" alt="OSINT Buddy Logo">
  </a>

  > *I have no data yet. It is a capital mistake to theorize before one has data. Insensibly
  > one begins to twist facts to suit theories, instead of theories to suit facts.*

  <h2><b>Introducing OSINTBuddy</b></h2>
  <p>
    Mine, merge, and map data for novel insights. Fetch data from different sources
    and returns the results as visual entities that you can explore step-by-step!
  </p>
<br/>

![osintbuddy-demo](https://github.com/jerlendds/osintbuddy/assets/29207058/5640a430-50f7-45df-9f75-8dd473dcdd1b)

  <br />
</p>

<details open="open">
<summary> 
<b>Table of Contents</b>
</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Introducing the OSINTBuddy Toolbox



OSINTBuddy is an OSINT tool in a very early beta which is distributed
for educational and investigative purposes, the person who has bought
or uses this tool is responsible for its proper use or actions committed,
jerlendds, the developer(s) of OSINTBuddy, are not responsible for the use
or the scope that people can have through this software.

[OSINTBuddy demo video](https://www.youtube.com/watch?v=XKBusfYGL4M)


### Key Features
- Simplified data fetching from multiple sources
- Visual representation of fetched data for easy understanding
- A powerful development platform that is open for contributions
- New plugin-based system for transforming data, check out the [osintbuddy](https://pypi.org/project/osintbuddy/) package. Documentation is coming soon.


&nbsp;&nbsp;&nbsp;\> **[https://docs.osintbuddy.com](https://docs-osintbuddy-com.vercel.app/)**

## [↑](#Introducing-the-OSINTBuddy-Toolbox)Getting Started

To start using OSINTBuddy, follow these simple installation steps:

### Installation

1. Clone the repo and submodules
   ```sh
   git clone --recurse-submodules https://github.com/jerlendds/osintbuddy.git
   cd osintbuddy
   ```
2. Install Docker

3. Start the stack with Docker:

   ```sh
   cp .env.example .env
   docker compose up
   ```

- **URLs**
  - Frontend: http://localhost:3000
  - Backend: http://localhost:5000/api/
  - Documentation: http://localhost:5000/docs -- http://localhost:5000/redoc
- Access OSINTBuddy through the URLs provided for frontend, backend, documentation, and more.

## [↑](#Introducing-the-OSINTBuddy-Toolbox)Roadmap
 
See our [trello board](https://trello.com/b/99Q70frX/) 
for a list of our upcoming features

See the [open issues](https://github.com/jerlendds/osintbuddy/issues)
for a list of requested features (and known issues).

## [↑](#Introducing-the-OSINTBuddy-Toolbox)Progress Notes

- [x] Website node
- [x] Google search node
- [x] Google cache search node
- [x] Google dorks
- [x] DNS node
- [x] URL node
- [x] IP node
- [x] CSE node
- [x] Username node

- [x] Added a plugin system
-  For this update you'll have to rebuild your docker containers. After that long wait you'll be rewarded with a newly released package: [osintbuddy](https://pypi.org/project/osintbuddy/)  
    The osintbuddy package allows for transforming data through a `@transform` decorator, which is applied to methods in the Plugin class.
- The transform decorator must have a label and, optionally, a [tabler-icons](https://tabler-icons.io/) icon name. You can manage node transformations and node creation easily through the API.
-  Basically these updates make it easier to create nodes and context menu options for a nodes transform options which are mapped to plugin methods.
- More documentation is coming soon when I have the time.
  Here's a video on the new update in the meantime: [Introducing OSINTBuddy: A plugin based Maltego alternative in beta](https://www.youtube.com/watch?v=XKBusfYGL4M)
  



## [↑](#Introducing-the-OSINTBuddy-Toolbox)Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/add-core-plugin`)
3. Commit your Changes (`git commit -m 'feat: add core plugin to osintbuddy app'`)
4. Push to the Branch (`git push origin feature/add-core-plugin`)
5. Open a Pull Request


## [↑](#Introducing-the-OSINTBuddy-Toolbox)License

[GNU AGPLv3](https://choosealicense.com/licenses/gpl-3.0/)

*Note, the [OSINTBuddy plugins package](https://github.com/jerlendds/osintbuddy-plugins) is MIT licensed*

[![Total Downloads](https://static.pepy.tech/badge/osintbuddy)](https://pepy.tech/project/osintbuddy)
[![Downloads](https://static.pepy.tech/badge/osintbuddy/week)](https://pepy.tech/project/osintbuddy)


## [↑](#Introducing-the-OSINTBuddy-Toolbox)Contact

Open an issue if you need to get in touch with me

- Project Link: [https://github.com/jerlendds/osintbuddy](https://github.com/jerlendds/osintbuddy)
- Plugins Package Link: [https://github.com/jerlendds/osintbuddy-plugins](https://github.com/jerlendds/osintbuddy-plugins)

[contributors-shield]: https://img.shields.io/github/contributors/jerlendds/osintbuddy.svg?style=for-the-badge
[contributors-url]: https://github.com/jerlendds/osintbuddy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jerlendds/osintbuddy.svg?style=for-the-badge
[forks-url]: https://github.com/jerlendds/osintbuddy/network/members
[stars-shield]: https://img.shields.io/github/stars/jerlendds/osintbuddy.svg?style=for-the-badge
[stars-url]: https://github.com/jerlendds/osintbuddy/stargazers
[issues-shield]: https://img.shields.io/github/issues/jerlendds/osintbuddy.svg?style=for-the-badge
[issues-url]: https://github.com/jerlendds/osintbuddy/issues
