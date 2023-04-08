---
tag: mitre/{{ technique.id }}
---

**{{technique.name}}**

Link: [{{technique.id}} - {{technique.name}}]({{technique.url}})
{% if technique.parent %}
Parent : [[{{technique.parent}}]]
{% else %}
Parent : None
{%endif%}

# Description

{{technique.description}}

# Tactics

{% for x in technique.tactics %}
[[{{ x }}]]
{% endfor %}

# Notes:

## Linux

Use Tool Template here

## Windows

Use Tool Template here
