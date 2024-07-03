<!-- This READM is based on the BEST-README-Template (https://github.com/othneildrew/Best-README-Template) -->
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- Add additional Badges. Some examples >
![Format Badge](https://github.com/iotaledger/template/workflows/Format/badge.svg "Format Badge")
![Audit Badge](https://github.com/iotaledger/template/workflows/Audit/badge.svg "Audit Badge")
![Clippy Badge](https://github.com/iotaledger/template/workflows/Clippy/badge.svg "Clippy Badge")
![BuildBadge](https://github.com/iotaledger/template/workflows/Build/badge.svg "Build Badge")
![Test Badge](https://github.com/iotaledger/template/workflows/Test/badge.svg "Test Badge")
![Coverage Badge](https://coveralls.io/repos/github/iotaledger/template/badge.svg "Coverage Badge")


<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="https://github.com/iotaledger/template">
        <img src="banner.png" alt="Banner">
    </a>
    <h3 align="center">IOTA-Blockchain</h3>
    <p align="center">
        project_description
        <br />
        <a href="https://wiki.iota.org"><strong>Explore the docs »</strong></a>
        <br />
        <br />
       <p></p>
</div>



<!-- TABLE OF CONTENTS -->
<!-- TODO 
Edit the ToC to your needs. If your project is part of the wiki, you should link directly to the Wiki where possible and remove unneeded sections to prevent duplicates 
-->




<!-- ABOUT THE PROJECT -->
## IOTA SANDBOX


To install and run IOTA Sandbox, you should install all requirement below:

1. A recent release of Docker
2. Docker Compose CLI plugin
3. sed
4. jd
5. Ports: 80 and 8062, make sure they available for Sandbox or you can change in the ports in `.env` file.


### After having all requirements, you can download Sandbox. The following command will download the latest version:
    
    mkdir iota-sandbox && cd iota-sandbox && curl -L https://github.com/iotaledger/iota-sandbox/releases/latest/download/iota_sandbox.tar.gz | tar -zx







<!-- GETTING STARTED -->
## RUN
Copy .env.example .env:

    cp .env.example .env

Start IOTA SandBox:

    docker compose up -d

Stop IOTA SandBox:

    docker compose down


<p align="right">(<a href="#top">back to top</a>)</p>

#### Document



_For more detail about installation of IOTA [SandBox](https://wiki.iota.org/iota-sandbox/getting-started/)_

<p align="right">(<a href="#top">back to top</a>)</p>
