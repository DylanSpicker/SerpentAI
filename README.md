![](https://s3.ca-central-1.amazonaws.com/serpent-ai-assets/SerpentFBCover.png)

# Serpent.AI - Game Agent Framework (Python)

[![](https://img.shields.io/badge/twitch-%40Serpent__AI-brightgreen.svg?colorB=6441a5&longCache=true)](https://www.twitch.tv/serpent_ai)
[![](https://img.shields.io/badge/twitch-%40Serpent__AI__Labs-brightgreen.svg?colorB=6441a5&longCache=true)](https://www.twitch.tv/serpent_ai_labs)
[![](https://img.shields.io/badge/youtube-SerpentAI-brightgreen.svg?colorB=ff0000&longCache=true)](https://www.youtube.com/c/SerpentAI)
[![](https://img.shields.io/badge/twitter-@Serpent__AI-brightgreen.svg?colorB=1da1f2&longCache=true)](https://twitter.com/Serpent_AI)
[![](https://img.shields.io/badge/patreon-donate-brightgreen.svg?colorB=f96854&longCache=true)](https://www.patreon.com/serpent_ai)  
[![](https://img.shields.io/badge/project-website-brightgreen.svg?colorB=1bcc6f&longCache=true)](http://serpent.ai)
[![](https://img.shields.io/badge/project-blog-brightgreen.svg?colorB=1bcc6f&longCache=true)](http://blog.serpent.ai)
[![](https://img.shields.io/badge/project-forums-brightgreen.svg?colorB=1bcc6f&longCache=true)](http://discuss.serpent.ai)
[![](https://img.shields.io/badge/project-wiki-brightgreen.svg?colorB=1bcc6f&longCache=true)](https://github.com/SerpentAI/SerpentAI/wiki)  
[![](https://img.shields.io/badge/pypi-v2018.1.2-brightgreen.svg?colorB=007ec6&longCache=true)]()
[![](https://img.shields.io/badge/python-3.6-brightgreen.svg?colorB=007ec6&longCache=true)]()
[![](https://img.shields.io/badge/license-MIT-brightgreen.svg?colorB=007ec6&longCache=true)]()

### Want to see the framework in action? The Serpent.AI Labs stream experiments 24/7 on [Twitch](https://www.twitch.tv/serpent_ai_labs)

### Join the newly created Serpent.AI community over at [http://discuss.serpent.ai](http://discuss.serpent.ai)

### Retroarch Launcher Fork
This repository contains my (WIP) fork of the SerpentAI library, to which I have added the ability to generate [Retroarch](http://www.retroarch.com/) game plugins. While still in development, the repository at this point opens up the ability to specify 'retroarch' in the `serpent generate game` command process. Retroarch is (essentially) a unified backend that allows for emulation cores to be added from a wide range of backends. The emulation spans most conceivable game consoles, making this an incredibly straightforward way to add retrogames, from any system, to your Serpent library. The plugin then requires the specification of a core and (optionally) a ROM path, which in turn allows you to add any core/ROM combination as a game easily through Serpent. 

I plan on adding a mechanism through which you can specify the corresponding system that you hope to emulate during the setup process, and have Serpent handle the correct download/locating of the core file if it does not already exist, but that will come later. Further, for now this has only been tested on Windows (running Windows10). If anyone has any issues/comments/etc. trying to install this launcher on other systems, please reach out and I can try to make other necessary changes!

In the current main repository for Serpent it is possible to add retroarch as an executable game, playing a little bit with how you set this up, but hopefully this provides an easy/accessible manner to add these games!

#### Set-up and Installation
In order to correctly launch a retroarch game, you need to have retroarch downloaded [(downlaod link)](http://www.retroarch.com/?page=platforms), and added to your PATH. You should be able to run `retroarch` and see the standard menu open to ensure that this has been setup correctly.

You will then need to install any cores that you wish to use, and take note of their corresponding directories (a parameter that will need to be specified during plugin development). 

The [standard set-up](https://github.com/SerpentAI/SerpentAI/wiki/Windows-Installation-Guide) can mostly be followed. However, instead of running:
```pip install SerpentAI```

you will need to install a local copy of the plugin. The easiest way (in my opinion) is to:
1. Clone this git repository locally. For example, assume that it is in: `C:/SerpentAI`
2. Run `pip install -e C:/SerpentAI/`
3. This will install this version to your system. The remaining setup of the modules can be accomplished as per the previous link.

#### Example Plugins
You can take a look at [DylanSpicker/SerpentTwentyFourtyEightGamePlugin](https://github.com/DylanSpicker/SerpentTwentyFourtyEightGamePlugin) for an example game plugin (which uses the 2048 core). I have additionally built a starter agent for 2048, [DylanSpicker/SerpentT48StarterGameAgentPlugin](https://github.com/DylanSpicker/SerpentT48StarterGameAgentPlugin), which implements a very simplistic DQN in Keras to illustrate the base that you may use.

### Standard Serpent README
Serpent.AI is a simple yet powerful, novel framework to assist developers in the creation of game agents. Turn ANY video game you own  into a sandbox environment ripe for experimentation, all with familiar Python code. The framework's _raison d'être_ is first and foremost to provide a valuable tool for Machine Learning & AI research. It also turns out to be ridiculously fun to use as a hobbyist (and dangerously addictive; a fair warning)!

The framework features a large assortment of supporting modules that provide solutions to commonly encountered scenarios when using video games as environments  as well as CLI tools to accelerate development. It provides some useful conventions but is absolutely NOT opiniated about what you put in your agents: Want to use the latest, cutting-edge deep reinforcement learning algorithm? ALLOWED. Want to use computer vision techniques, image processing and trigonometry? ALLOWED. Want to randomly press the Left or Right buttons? _sigh_ ALLOWED. To top it all off, Serpent.AI was designed to be entirely plugin-based (for both game support and game agents) so your experiments are actually portable and distributable to your peers and random strangers on the Internet.

You'll also be glad to hear that all 3 major OSes are supported: Linux, Windows & macOS.

![](https://s3.ca-central-1.amazonaws.com/serpent-ai-assets/demo_isaac.gif)

_Experiment: Game agent learning to defeat Monstro (The Binding of Isaac: Afterbirth+)_

## Background

The project was born out of admiration for / frustration with [OpenAI Universe](https://github.com/openai/universe). The idea is perfect, let's be honest, but some implementation details leave a lot to be desired. From these, the core tennets of the framework were established:

1. Thou shall run natively. Thou shalt not use Docker containers or VNC servers.
2. Thou shall allow a user to bring their own games. Thou shalt not wait for licensing deals and special game APIs.
3. Thou shall encourage diverse and creative approaches. Thou shalt not only enable AI flavors of the month.

_Want to know more about how Serpent.AI came to be? Read [The Story Behind Serpent.AI](http://blog.serpent.ai/the-story-behind-serpent-ai/) on the blog!_

## Documentation

Guides, tutorials and videos are being produced and added to the [GitHub Wiki](https://github.com/SerpentAI/SerpentAI/wiki). It currently is the official source of documentation.

## Getting Help

If you encounter a bug, crash or edge case while using the Serpent.AI framework, you are encouraged to create a GitHub [issue](https://github.com/SerpentAI/SerpentAI/issues/new). If you do so, please make sure to provide as much context as possible. You can also ask your questions and get help from the community over at [http://discuss.serpent.ai](http://discuss.serpent.ai). Installation problems should be directed towards the discussion boards and not GitHub issues.

## Showcasing your Work

Have you built something cool using Serpent.AI? Want to give the community progress updates? Share your repositories and videos over at [http://discuss.serpent.ai](http://discuss.serpent.ai). There is also a [wiki page](https://github.com/SerpentAI/SerpentAI/wiki/Community-Plugin-Showcase) reserved for showcasing your plugins!

![](https://s3.ca-central-1.amazonaws.com/serpent-ai-assets/demo_ymbab.gif)

_Experiment: Game agent learning to match tiles (You Must Build a Boat)_

Serpent.AI is the love child of [@nbrochu](https://github.com/nbrochu)'s passion for science & experimentation, programming and video games.

_Business Contact: info@serpent.ai_
