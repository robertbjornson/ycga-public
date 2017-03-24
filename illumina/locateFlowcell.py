#!/home/rob/Installed/anaconda3/bin/python

import glob, sys

runlocs=["/ycga-gpfs/sequencers/panfs/sequencers*",
"/SAY/archive/YCGA-729009-YCGA/archive/panfs/sequencers*",
"/ycga-ba/sequencers*",
"/SAY/archive/YCGA-729009-YCGA/archive/ycga-ba/sequencers*",
"/ycga-gpfs/sequencers/illumina",
"/SAY/archive/YCGA-729009-YCGA/archive/ycga-gpfs/sequencers/illumina"
]

USAGE='''
Usage: locateFlowcell.py pat

E.g.
$ locateFlowcell.py ACACD5AN

This utility finds illumina sequencing runs, given a pattern representing a partial run name.
Both active and archive storage are searched, and all locations are returned.
'''

def locateRun(pat):
    got=[]
    for runloc in runlocs:
        chk=runloc+"/sequencer?/runs/*%s*" % pat
        #/home/rob/archive/archive/panfs/sequencers4/sequencerW/runs
        #print ("checking " + chk)
        got+=glob.glob(chk)
    return got

if __name__=='__main__':
    if len(sys.argv)<2:
        print (USAGE)
        sys.exit(0)

    got=locateRun(sys.argv[1])
    for run in got:
        print(run)

