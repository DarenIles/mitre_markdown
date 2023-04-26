# MITRE in Markdown

If you need your Mitre data in markdown...

Using Mitre version V13  https://attack.mitre.org/

Works expecially well with obsidian https://obsidian.md/

![Screenshot](screenshot.png)

## To use

Just clone this repo.

Markdown files are here: [Output](./output)

## To refresh

1. Get the latest MITRE version (replacing version number)  [[https://attack.mitre.org/docs/enterprise-attack-v13.0/enterprise-attack-v13.0-techniques.xlsx]]

2.  Convert to csv

3.  Make sure the csv field mapping match in the [script](generate.py)

4.  Run

```
python3 generate.py
```

## Contributing

PRs accepted.