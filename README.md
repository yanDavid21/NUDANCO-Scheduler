# NUDANCO Scheduler

## Summary

Given a dance roster, generate a dance schedule that does _not_ have any "overlapping dances". Overlapping dances are 2 dances back to back that share dancers.

## Usage

In this project directory:
`python index.py <file-name>`

Using the command line, run the script and give the file name of a dance roster. The dance roster should be a csv files (spreadsheets) that contains the names of the dances in the first row. And the names of the dances for each dance in the respective column. Example dance roster csv files can be found in the data/ folder.

Note: Please install python if you do not have it installed. Mac users, you should install python3 and use the command `python3` instead of `python` since that usually refers to python 2.

Tip: You can run the script multiple times as it is non-deterministic, aka. generates a random/different valid schedule each time. So if you need some certain dances to be separated beyond being an overlapping dance, run the script multiple times.

Example output:

```
["Tyler's Contemporary", "Maya's Contemporary", "Maggie & Caroline's Contemporary", "Carly & Shannon's Jazz", "Caitlin's Ballet"]
Intermission
["Nadia's Contemporary", "Regan's Hard Shoe", "Amanda & Bianca's Contemporary", "Alex & Maeve's Light Shoe", "Meghan's Contemporary", "Jessica's Tap"]
```

## Purpose

This scheduler was made for the intent of scheduling dances for NUDanco's biannual showcase. NUDanco's showcases usually contains multiple dances that share dancers. Each dance often have unique costumes. So dances that share dancers cannot be scheduled next to each other since dancers will not have time to do a costume change. I saw my friend, Adrianna Liu, who was on E-board of the club at the time scheduling these dances by hand. It seemed to be a very time intensive process since each permutation had to be manually verified and also had a high failure time, ie. finding out a permutation to be a invalid one can take a long time.
