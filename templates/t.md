
|Field|Value|
|---|---|
|Tactic|[[{{ technique.tactics|join(', ') }}]]|
|Technique Name|**{{technique.name}}**|
|ID|**{{technique.id}}**|
|Parent|{% if technique.parent %}[[{{technique.parent}}]]{% else %}Parent : None{%endif%}|
|Link|[{{technique.id}} - {{technique.name}}]({{technique.url}})|

# Description

{{technique.description}}
