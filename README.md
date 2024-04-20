# Matterbridge for Home Assistant

## NO, THIS IS NOT ABOUT THE MATTER RADIO HOME APPLIANCE SYSTEM
## NO, THIS WILL NOT WORK FOR YOUR USECASE

This is an integration for [Matterbridge](https://github.com/42wim/matterbridge) notifications. It uses a custom endpoint. Ask [@niyawe](https://github.com/niyawe) what the hell is going on on the other side.

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

----

### Contents

 * [Functionality](#functionality)
 * [Installation](#installation)
 * [Configuration](#configuration)
 * [Installation and Configuration Summary](#installation-and-configuration-summary)
 * [Usage](#usage)
 * [License](#license)

----

### Functionality

This integration is based on [Facebook Messenger integration by emes30](https://github.com/emes30/facebook_messenger/).

----

### Installation

Copy the repository as `matterbridge_notify` into the `config\custom_components` folder of your Home Assistant instance, configure and restart.

----

### Configuration

This integration exposes itself as a <a href="https://www.home-assistant.io/integrations/notify/" target="_blank">notifications integration</a>, and can be configured by adding this snippet in your `configuration.yaml` file:

```yaml
notify:
  name: matterbridge
  platform: matterbridge_notify
  url: <YOUR URL>
  kes: <YOUR KEY>
```

Replace `<YOUR_URL>` with the URL to your webservice

Replace `<YOUR_KEY>` with your key, use secrets.yaml for better protection.

Restart Home Assistant to load your configuration.

---

### Installation and Configuration Summary

Quick summary to get things working:

- Install **matterbridge_notify** integration
- Create a `notify` entity, use your url and key
- Restart Home Assistant
- Start adding the new entity to your automations & scripts

----

### Usage

```yaml
  action:
    - service: notify.matterbridge
      data:
        message: "Hello World"
```

You can also test it in Developer Tools, under Services tab.

----

### License

This software is released under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT license</a>.
