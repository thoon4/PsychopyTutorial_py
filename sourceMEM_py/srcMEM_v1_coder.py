#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on 8월 16, 2020, at 17:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.1.2')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'srcMEM_v1'  # from the Builder filename that created this script
expInfo = {'SN': '99', 'Gender': 'f'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['SN'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Dropbox\\3.Python\\02.PsychoPy\\sourceMEM\\srcMEM_v1_bd.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='monitor_v1', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
startM = visual.TextStim(win=win, name='startM',
    text='실험을 시작합니다.\n\n본 실험은 3개의 과제로 구성되어 있습니다.\n\n1) 학습 과제: 제시되는 그림과 위치를 연합 학습합니다.\n\n2) 스트룹 과제: 제시되는 단어의 의미에 해당되는 색을 반응합니다.\n\n3) 검사: 학습하였던 그림-위치 목록의 기억을 검사합니다.\n       제시되는 그림이 어느 위치에 제시되었는지 반응해주세요.\n\n시작하려면 "space"를 누르세요.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startM_resp = keyboard.Keyboard()

# Initialize components for Routine "inst1"
inst1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='학습 과제를 시작합니다.\n\n제시되는 물체와 위치를 함께 외워주세요.\n동시에, 물체가 생물인지, 비생물인지 반응해주세요.\n\n생물이면 "z", 비생물이면 "m"을 눌러주세요.\n\n시작하려면 "space"키를 누르세요.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
insrt1_resp = keyboard.Keyboard()

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',units='norm', 
    size=(0.031250, 0.055556),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rect1_1 = visual.Rect(
    win=win, name='rect1_1',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(-0.5, 0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
rect1_2 = visual.Rect(
    win=win, name='rect1_2',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(0.5, 0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
rect1_3 = visual.Rect(
    win=win, name='rect1_3',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(-0.5, -0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
rect1_4 = visual.Rect(
    win=win, name='rect1_4',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(0.5, -0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
LearnIM = visual.ImageStim(
    win=win,
    name='LearnIM', units='norm', 
    image='sin', mask=None,
    ori=0 , pos=[0,0], size=(0.311, 0.553),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
t1_resp = keyboard.Keyboard()

# Initialize components for Routine "break_1"
break_1Clock = core.Clock()
maxBT = 30

b1_inst = visual.TextStim(win=win, name='b1_inst',
    text='쉬는 시간입니다.\n\n눈과 손의 피로를 풀어주세요.\n\n아래의 시간이 끝나면 자동으로 다음 과제가 시작됩니다.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
b1_timeRemaining = visual.TextStim(win=win, name='b1_timeRemaining',
    text='default text',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
b1_resp = keyboard.Keyboard()

# Initialize components for Routine "inst2"
inst2Clock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='스트룹 과제를 시작합니다.\n\n"빨강, 초록, 파랑"이라는 단어가 제시됩니다.\n\n단어의 의미는 무시하고, 단어의 색에 해당되는 키를 누르세요.\n\n빨강 : leftArrow\n\n초록 : downArrow\n\n파랑 : rightArrow\n\n\n시작하려면 "space"를 누르세요.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
insrt2_resp = keyboard.Keyboard()

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
fix2 = visual.ShapeStim(
    win=win, name='fix2', vertices='cross',units='pix', 
    size=(30, 30),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
stroop = visual.TextStim(win=win, name='stroop',
    text='default text',
    font='NotoSansCJKkr-Medium',
    units='pix', pos=(0, 0), height=50, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
t2_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg = ''
corr = []
feedbackM = visual.TextStim(win=win, name='feedbackM',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=30, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
b2_inst = visual.TextStim(win=win, name='b2_inst',
    text='쉬는 시간입니다.\n\n눈과 손의 피로를 풀어주세요.\n\n아래의 시간이 끝나면 자동으로 다음 과제가 시작됩니다.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
b2_timeRemaining = visual.TextStim(win=win, name='b2_timeRemaining',
    text='default text',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
b2_resp = keyboard.Keyboard()

# Initialize components for Routine "inst3"
inst3Clock = core.Clock()
instr3 = visual.TextStim(win=win, name='instr3',
    text='검사 과제를 시작합니다.\n\n제시되는 물체를 보고 물체가 어느 위치에 제시되었었는지 키를 눌러주세요.\n\n시작하려면 "space"를 누르세요.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
insrt3_resp = keyboard.Keyboard()

# Initialize components for Routine "trial3"
trial3Clock = core.Clock()
fix3 = visual.ShapeStim(
    win=win, name='fix3', vertices='cross',units='norm', 
    size=(0.031250, 0.055556),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[1,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
rect3_1 = visual.Rect(
    win=win, name='rect3_1',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(-0.5, 0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
rect3_2 = visual.Rect(
    win=win, name='rect3_2',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(0.5, 0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
rect3_3 = visual.Rect(
    win=win, name='rect3_3',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(-0.5, -0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
rect3_4 = visual.Rect(
    win=win, name='rect3_4',units='norm', 
    width=(0.312, 0.554)[0], height=(0.312, 0.554)[1],
    ori=0, pos=(0.5, -0.5),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
testIM = visual.ImageStim(
    win=win,
    name='testIM', units='norm', 
    image='sin', mask=None,
    ori=0 , pos=[0,0], size=(0.311, 0.553),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
t3_resp = keyboard.Keyboard()

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()
b3_inst = visual.TextStim(win=win, name='b3_inst',
    text='쉬는 시간입니다.\n\n눈과 손의 피로를 풀어주세요.\n\n아래의 시간이 끝나면 자동으로 다음 과제가 시작됩니다.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
b3_timeRemaining = visual.TextStim(win=win, name='b3_timeRemaining',
    text='default text',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
b3_resp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
endM = visual.TextStim(win=win, name='endM',
    text='실험이 종료되었습니다.\n\n참여해주셔서 감사합니다.\n\n실험자를 불러주세요.',
    font='NotoSansCJKkr-Medium',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endM_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
startM_resp.keys = []
startM_resp.rt = []
_startM_resp_allKeys = []
# keep track of which components have finished
startComponents = [startM, startM_resp]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startM* updates
    if startM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startM.frameNStart = frameN  # exact frame index
        startM.tStart = t  # local t and not account for scr refresh
        startM.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startM, 'tStartRefresh')  # time at next scr refresh
        startM.setAutoDraw(True)
    
    # *startM_resp* updates
    waitOnFlip = False
    if startM_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startM_resp.frameNStart = frameN  # exact frame index
        startM_resp.tStart = t  # local t and not account for scr refresh
        startM_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startM_resp, 'tStartRefresh')  # time at next scr refresh
        startM_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startM_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startM_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startM_resp.status == STARTED and not waitOnFlip:
        theseKeys = startM_resp.getKeys(keyList=['space'], waitRelease=False)
        _startM_resp_allKeys.extend(theseKeys)
        if len(_startM_resp_allKeys):
            startM_resp.keys = _startM_resp_allKeys[-1].name  # just the last key pressed
            startM_resp.rt = _startM_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst1"-------
continueRoutine = True
# update component parameters for each repeat
insrt1_resp.keys = []
insrt1_resp.rt = []
_insrt1_resp_allKeys = []
# keep track of which components have finished
inst1Components = [instr1, insrt1_resp]
for thisComponent in inst1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst1"-------
while continueRoutine:
    # get current time
    t = inst1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *insrt1_resp* updates
    waitOnFlip = False
    if insrt1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insrt1_resp.frameNStart = frameN  # exact frame index
        insrt1_resp.tStart = t  # local t and not account for scr refresh
        insrt1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insrt1_resp, 'tStartRefresh')  # time at next scr refresh
        insrt1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insrt1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insrt1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insrt1_resp.status == STARTED and not waitOnFlip:
        theseKeys = insrt1_resp.getKeys(keyList=['space'], waitRelease=False)
        _insrt1_resp_allKeys.extend(theseKeys)
        if len(_insrt1_resp_allKeys):
            insrt1_resp.keys = _insrt1_resp_allKeys[-1].name  # just the last key pressed
            insrt1_resp.rt = _insrt1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst1"-------
for thisComponent in inst1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
t1_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('t1_design.xlsx'),
    seed=None, name='t1_trials')
thisExp.addLoop(t1_trials)  # add the loop to the experiment
thisT1_trial = t1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisT1_trial.rgb)
if thisT1_trial != None:
    for paramName in thisT1_trial:
        exec('{} = thisT1_trial[paramName]'.format(paramName))

for thisT1_trial in t1_trials:
    currentLoop = t1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisT1_trial.rgb)
    if thisT1_trial != None:
        for paramName in thisT1_trial:
            exec('{} = thisT1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    LearnIM.setPos((LocPosX, LocPosY))
    LearnIM.setImage(IMname)
    t1_resp.keys = []
    t1_resp.rt = []
    _t1_resp_allKeys = []
    # keep track of which components have finished
    trial1Components = [fix1, rect1_1, rect1_2, rect1_3, rect1_4, LearnIM, t1_resp]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            fix1.setAutoDraw(True)
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
                fix1.setAutoDraw(False)
        
        # *rect1_1* updates
        if rect1_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect1_1.frameNStart = frameN  # exact frame index
            rect1_1.tStart = t  # local t and not account for scr refresh
            rect1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect1_1, 'tStartRefresh')  # time at next scr refresh
            rect1_1.setAutoDraw(True)
        if rect1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect1_1.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                rect1_1.tStop = t  # not accounting for scr refresh
                rect1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect1_1, 'tStopRefresh')  # time at next scr refresh
                rect1_1.setAutoDraw(False)
        
        # *rect1_2* updates
        if rect1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect1_2.frameNStart = frameN  # exact frame index
            rect1_2.tStart = t  # local t and not account for scr refresh
            rect1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect1_2, 'tStartRefresh')  # time at next scr refresh
            rect1_2.setAutoDraw(True)
        if rect1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect1_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                rect1_2.tStop = t  # not accounting for scr refresh
                rect1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect1_2, 'tStopRefresh')  # time at next scr refresh
                rect1_2.setAutoDraw(False)
        
        # *rect1_3* updates
        if rect1_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect1_3.frameNStart = frameN  # exact frame index
            rect1_3.tStart = t  # local t and not account for scr refresh
            rect1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect1_3, 'tStartRefresh')  # time at next scr refresh
            rect1_3.setAutoDraw(True)
        if rect1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect1_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                rect1_3.tStop = t  # not accounting for scr refresh
                rect1_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect1_3, 'tStopRefresh')  # time at next scr refresh
                rect1_3.setAutoDraw(False)
        
        # *rect1_4* updates
        if rect1_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect1_4.frameNStart = frameN  # exact frame index
            rect1_4.tStart = t  # local t and not account for scr refresh
            rect1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect1_4, 'tStartRefresh')  # time at next scr refresh
            rect1_4.setAutoDraw(True)
        if rect1_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rect1_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                rect1_4.tStop = t  # not accounting for scr refresh
                rect1_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rect1_4, 'tStopRefresh')  # time at next scr refresh
                rect1_4.setAutoDraw(False)
        
        # *LearnIM* updates
        if LearnIM.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            LearnIM.frameNStart = frameN  # exact frame index
            LearnIM.tStart = t  # local t and not account for scr refresh
            LearnIM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LearnIM, 'tStartRefresh')  # time at next scr refresh
            LearnIM.setAutoDraw(True)
        if LearnIM.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LearnIM.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                LearnIM.tStop = t  # not accounting for scr refresh
                LearnIM.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LearnIM, 'tStopRefresh')  # time at next scr refresh
                LearnIM.setAutoDraw(False)
        
        # *t1_resp* updates
        waitOnFlip = False
        if t1_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            t1_resp.frameNStart = frameN  # exact frame index
            t1_resp.tStart = t  # local t and not account for scr refresh
            t1_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t1_resp, 'tStartRefresh')  # time at next scr refresh
            t1_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(t1_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(t1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if t1_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > t1_resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                t1_resp.tStop = t  # not accounting for scr refresh
                t1_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(t1_resp, 'tStopRefresh')  # time at next scr refresh
                t1_resp.status = FINISHED
        if t1_resp.status == STARTED and not waitOnFlip:
            theseKeys = t1_resp.getKeys(keyList=['z', 'm'], waitRelease=False)
            _t1_resp_allKeys.extend(theseKeys)
            if len(_t1_resp_allKeys):
                t1_resp.keys = _t1_resp_allKeys[-1].name  # just the last key pressed
                t1_resp.rt = _t1_resp_allKeys[-1].rt
                # was this correct?
                if (t1_resp.keys == str(CorrAnsCat)) or (t1_resp.keys == CorrAnsCat):
                    t1_resp.corr = 1
                else:
                    t1_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if t1_resp.keys in ['', [], None]:  # No response was made
        t1_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAnsCat).lower() == 'none':
           t1_resp.corr = 1;  # correct non-response
        else:
           t1_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for t1_trials (TrialHandler)
    t1_trials.addData('t1_resp.keys',t1_resp.keys)
    t1_trials.addData('t1_resp.corr', t1_resp.corr)
    if t1_resp.keys != None:  # we had a response
        t1_trials.addData('t1_resp.rt', t1_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 't1_trials'


# ------Prepare to start Routine "break_1"-------
continueRoutine = True
# update component parameters for each repeat
b1_resp.keys = []
b1_resp.rt = []
_b1_resp_allKeys = []
# keep track of which components have finished
break_1Components = [b1_inst, b1_timeRemaining, b1_resp]
for thisComponent in break_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_1"-------
while continueRoutine:
    # get current time
    t = break_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    b1_time = int(maxBT - break_1Clock.getTime())
    
    
    # *b1_inst* updates
    if b1_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b1_inst.frameNStart = frameN  # exact frame index
        b1_inst.tStart = t  # local t and not account for scr refresh
        b1_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b1_inst, 'tStartRefresh')  # time at next scr refresh
        b1_inst.setAutoDraw(True)
    if b1_inst.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b1_inst.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b1_inst.tStop = t  # not accounting for scr refresh
            b1_inst.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b1_inst, 'tStopRefresh')  # time at next scr refresh
            b1_inst.setAutoDraw(False)
    
    # *b1_timeRemaining* updates
    if b1_timeRemaining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b1_timeRemaining.frameNStart = frameN  # exact frame index
        b1_timeRemaining.tStart = t  # local t and not account for scr refresh
        b1_timeRemaining.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b1_timeRemaining, 'tStartRefresh')  # time at next scr refresh
        b1_timeRemaining.setAutoDraw(True)
    if b1_timeRemaining.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b1_timeRemaining.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b1_timeRemaining.tStop = t  # not accounting for scr refresh
            b1_timeRemaining.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b1_timeRemaining, 'tStopRefresh')  # time at next scr refresh
            b1_timeRemaining.setAutoDraw(False)
    if b1_timeRemaining.status == STARTED:  # only update if drawing
        b1_timeRemaining.setText('남은 시간: {time}'.format(time=b1_time), log=False)
    
    # *b1_resp* updates
    waitOnFlip = False
    if b1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b1_resp.frameNStart = frameN  # exact frame index
        b1_resp.tStart = t  # local t and not account for scr refresh
        b1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b1_resp, 'tStartRefresh')  # time at next scr refresh
        b1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(b1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(b1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if b1_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b1_resp.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b1_resp.tStop = t  # not accounting for scr refresh
            b1_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b1_resp, 'tStopRefresh')  # time at next scr refresh
            b1_resp.status = FINISHED
    if b1_resp.status == STARTED and not waitOnFlip:
        theseKeys = b1_resp.getKeys(keyList=['space'], waitRelease=False)
        _b1_resp_allKeys.extend(theseKeys)
        if len(_b1_resp_allKeys):
            b1_resp.keys = _b1_resp_allKeys[-1].name  # just the last key pressed
            b1_resp.rt = _b1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_1"-------
for thisComponent in break_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "break_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst2"-------
continueRoutine = True
# update component parameters for each repeat
insrt2_resp.keys = []
insrt2_resp.rt = []
_insrt2_resp_allKeys = []
# keep track of which components have finished
inst2Components = [instr2, insrt2_resp]
for thisComponent in inst2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst2"-------
while continueRoutine:
    # get current time
    t = inst2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *insrt2_resp* updates
    waitOnFlip = False
    if insrt2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insrt2_resp.frameNStart = frameN  # exact frame index
        insrt2_resp.tStart = t  # local t and not account for scr refresh
        insrt2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insrt2_resp, 'tStartRefresh')  # time at next scr refresh
        insrt2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insrt2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insrt2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insrt2_resp.status == STARTED and not waitOnFlip:
        theseKeys = insrt2_resp.getKeys(keyList=['space'], waitRelease=False)
        _insrt2_resp_allKeys.extend(theseKeys)
        if len(_insrt2_resp_allKeys):
            insrt2_resp.keys = _insrt2_resp_allKeys[-1].name  # just the last key pressed
            insrt2_resp.rt = _insrt2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst2"-------
for thisComponent in inst2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
t2_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('t2_design.xlsx'),
    seed=None, name='t2_trials')
thisExp.addLoop(t2_trials)  # add the loop to the experiment
thisT2_trial = t2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisT2_trial.rgb)
if thisT2_trial != None:
    for paramName in thisT2_trial:
        exec('{} = thisT2_trial[paramName]'.format(paramName))

for thisT2_trial in t2_trials:
    currentLoop = t2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisT2_trial.rgb)
    if thisT2_trial != None:
        for paramName in thisT2_trial:
            exec('{} = thisT2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    # update component parameters for each repeat
    stroop.setColor(letterColor, colorSpace='rgb')
    stroop.setText(word)
    t2_resp.keys = []
    t2_resp.rt = []
    _t2_resp_allKeys = []
    # keep track of which components have finished
    trial2Components = [fix2, stroop, t2_resp]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix2* updates
        if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix2.frameNStart = frameN  # exact frame index
            fix2.tStart = t  # local t and not account for scr refresh
            fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
            fix2.setAutoDraw(True)
        if fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix2.tStop = t  # not accounting for scr refresh
                fix2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
                fix2.setAutoDraw(False)
        
        # *stroop* updates
        if stroop.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stroop.frameNStart = frameN  # exact frame index
            stroop.tStart = t  # local t and not account for scr refresh
            stroop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stroop, 'tStartRefresh')  # time at next scr refresh
            stroop.setAutoDraw(True)
        if stroop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stroop.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                stroop.tStop = t  # not accounting for scr refresh
                stroop.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stroop, 'tStopRefresh')  # time at next scr refresh
                stroop.setAutoDraw(False)
        
        # *t2_resp* updates
        waitOnFlip = False
        if t2_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            t2_resp.frameNStart = frameN  # exact frame index
            t2_resp.tStart = t  # local t and not account for scr refresh
            t2_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t2_resp, 'tStartRefresh')  # time at next scr refresh
            t2_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(t2_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(t2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if t2_resp.status == STARTED and not waitOnFlip:
            theseKeys = t2_resp.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _t2_resp_allKeys.extend(theseKeys)
            if len(_t2_resp_allKeys):
                t2_resp.keys = _t2_resp_allKeys[-1].name  # just the last key pressed
                t2_resp.rt = _t2_resp_allKeys[-1].rt
                # was this correct?
                if (t2_resp.keys == str(corrAns)) or (t2_resp.keys == corrAns):
                    t2_resp.corr = 1
                else:
                    t2_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if t2_resp.keys in ['', [], None]:  # No response was made
        t2_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           t2_resp.corr = 1;  # correct non-response
        else:
           t2_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for t2_trials (TrialHandler)
    t2_trials.addData('t2_resp.keys',t2_resp.keys)
    t2_trials.addData('t2_resp.corr', t2_resp.corr)
    if t2_resp.keys != None:  # we had a response
        t2_trials.addData('t2_resp.rt', t2_resp.rt)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if t2_resp.corr:#stored on last run routine
      msg="맞았습니다! RT=%.3f" %(t2_resp.rt)
    else:
      msg="틀렸습니다"
    
    # track (up to) the last 5 trials
    corr.append(t2_resp.corr)
    nCorr = sum(corr[-5:])
    nResps = len(corr[-5:])
    msg += "({} out of {} correct)".format(nCorr, nResps)
    feedbackM.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackM]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackM* updates
        if feedbackM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackM.frameNStart = frameN  # exact frame index
            feedbackM.tStart = t  # local t and not account for scr refresh
            feedbackM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackM, 'tStartRefresh')  # time at next scr refresh
            feedbackM.setAutoDraw(True)
        if feedbackM.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackM.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedbackM.tStop = t  # not accounting for scr refresh
                feedbackM.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackM, 'tStopRefresh')  # time at next scr refresh
                feedbackM.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 't2_trials'


# ------Prepare to start Routine "break_2"-------
continueRoutine = True
# update component parameters for each repeat
b2_resp.keys = []
b2_resp.rt = []
_b2_resp_allKeys = []
# keep track of which components have finished
break_2Components = [b2_inst, b2_timeRemaining, b2_resp]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    b2_time = int(maxBT - break_2Clock.getTime())
    
    # *b2_inst* updates
    if b2_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b2_inst.frameNStart = frameN  # exact frame index
        b2_inst.tStart = t  # local t and not account for scr refresh
        b2_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b2_inst, 'tStartRefresh')  # time at next scr refresh
        b2_inst.setAutoDraw(True)
    if b2_inst.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b2_inst.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b2_inst.tStop = t  # not accounting for scr refresh
            b2_inst.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b2_inst, 'tStopRefresh')  # time at next scr refresh
            b2_inst.setAutoDraw(False)
    
    # *b2_timeRemaining* updates
    if b2_timeRemaining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b2_timeRemaining.frameNStart = frameN  # exact frame index
        b2_timeRemaining.tStart = t  # local t and not account for scr refresh
        b2_timeRemaining.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b2_timeRemaining, 'tStartRefresh')  # time at next scr refresh
        b2_timeRemaining.setAutoDraw(True)
    if b2_timeRemaining.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b2_timeRemaining.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b2_timeRemaining.tStop = t  # not accounting for scr refresh
            b2_timeRemaining.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b2_timeRemaining, 'tStopRefresh')  # time at next scr refresh
            b2_timeRemaining.setAutoDraw(False)
    if b2_timeRemaining.status == STARTED:  # only update if drawing
        b2_timeRemaining.setText('남은 시간: {time}'.format(time=b2_time), log=False)
    
    # *b2_resp* updates
    waitOnFlip = False
    if b2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b2_resp.frameNStart = frameN  # exact frame index
        b2_resp.tStart = t  # local t and not account for scr refresh
        b2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b2_resp, 'tStartRefresh')  # time at next scr refresh
        b2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(b2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(b2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if b2_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b2_resp.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b2_resp.tStop = t  # not accounting for scr refresh
            b2_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b2_resp, 'tStopRefresh')  # time at next scr refresh
            b2_resp.status = FINISHED
    if b2_resp.status == STARTED and not waitOnFlip:
        theseKeys = b2_resp.getKeys(keyList=['space'], waitRelease=False)
        _b2_resp_allKeys.extend(theseKeys)
        if len(_b2_resp_allKeys):
            b2_resp.keys = _b2_resp_allKeys[-1].name  # just the last key pressed
            b2_resp.rt = _b2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "break_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst3"-------
continueRoutine = True
# update component parameters for each repeat
insrt3_resp.keys = []
insrt3_resp.rt = []
_insrt3_resp_allKeys = []
# keep track of which components have finished
inst3Components = [instr3, insrt3_resp]
for thisComponent in inst3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst3"-------
while continueRoutine:
    # get current time
    t = inst3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr3* updates
    if instr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr3.frameNStart = frameN  # exact frame index
        instr3.tStart = t  # local t and not account for scr refresh
        instr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr3, 'tStartRefresh')  # time at next scr refresh
        instr3.setAutoDraw(True)
    
    # *insrt3_resp* updates
    waitOnFlip = False
    if insrt3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        insrt3_resp.frameNStart = frameN  # exact frame index
        insrt3_resp.tStart = t  # local t and not account for scr refresh
        insrt3_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(insrt3_resp, 'tStartRefresh')  # time at next scr refresh
        insrt3_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(insrt3_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(insrt3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if insrt3_resp.status == STARTED and not waitOnFlip:
        theseKeys = insrt3_resp.getKeys(keyList=['space'], waitRelease=False)
        _insrt3_resp_allKeys.extend(theseKeys)
        if len(_insrt3_resp_allKeys):
            insrt3_resp.keys = _insrt3_resp_allKeys[-1].name  # just the last key pressed
            insrt3_resp.rt = _insrt3_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst3"-------
for thisComponent in inst3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "inst3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
t3_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('t1_design.xlsx'),
    seed=None, name='t3_trials')
thisExp.addLoop(t3_trials)  # add the loop to the experiment
thisT3_trial = t3_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisT3_trial.rgb)
if thisT3_trial != None:
    for paramName in thisT3_trial:
        exec('{} = thisT3_trial[paramName]'.format(paramName))

for thisT3_trial in t3_trials:
    currentLoop = t3_trials
    # abbreviate parameter names if possible (e.g. rgb = thisT3_trial.rgb)
    if thisT3_trial != None:
        for paramName in thisT3_trial:
            exec('{} = thisT3_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial3"-------
    continueRoutine = True
    # update component parameters for each repeat
    testIM.setPos((0, 0))
    testIM.setImage(IMname)
    t3_resp.keys = []
    t3_resp.rt = []
    _t3_resp_allKeys = []
    # keep track of which components have finished
    trial3Components = [fix3, rect3_1, rect3_2, rect3_3, rect3_4, testIM, t3_resp]
    for thisComponent in trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial3"-------
    while continueRoutine:
        # get current time
        t = trial3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix3* updates
        if fix3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix3.frameNStart = frameN  # exact frame index
            fix3.tStart = t  # local t and not account for scr refresh
            fix3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix3, 'tStartRefresh')  # time at next scr refresh
            fix3.setAutoDraw(True)
        
        # *rect3_1* updates
        if rect3_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect3_1.frameNStart = frameN  # exact frame index
            rect3_1.tStart = t  # local t and not account for scr refresh
            rect3_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect3_1, 'tStartRefresh')  # time at next scr refresh
            rect3_1.setAutoDraw(True)
        
        # *rect3_2* updates
        if rect3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect3_2.frameNStart = frameN  # exact frame index
            rect3_2.tStart = t  # local t and not account for scr refresh
            rect3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect3_2, 'tStartRefresh')  # time at next scr refresh
            rect3_2.setAutoDraw(True)
        
        # *rect3_3* updates
        if rect3_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect3_3.frameNStart = frameN  # exact frame index
            rect3_3.tStart = t  # local t and not account for scr refresh
            rect3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect3_3, 'tStartRefresh')  # time at next scr refresh
            rect3_3.setAutoDraw(True)
        
        # *rect3_4* updates
        if rect3_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            rect3_4.frameNStart = frameN  # exact frame index
            rect3_4.tStart = t  # local t and not account for scr refresh
            rect3_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect3_4, 'tStartRefresh')  # time at next scr refresh
            rect3_4.setAutoDraw(True)
        
        # *testIM* updates
        if testIM.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            testIM.frameNStart = frameN  # exact frame index
            testIM.tStart = t  # local t and not account for scr refresh
            testIM.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testIM, 'tStartRefresh')  # time at next scr refresh
            testIM.setAutoDraw(True)
        
        # *t3_resp* updates
        waitOnFlip = False
        if t3_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            t3_resp.frameNStart = frameN  # exact frame index
            t3_resp.tStart = t  # local t and not account for scr refresh
            t3_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t3_resp, 'tStartRefresh')  # time at next scr refresh
            t3_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(t3_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(t3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if t3_resp.status == STARTED and not waitOnFlip:
            theseKeys = t3_resp.getKeys(keyList=['num_4', 'num_5', 'num_1', 'num_2'], waitRelease=False)
            _t3_resp_allKeys.extend(theseKeys)
            if len(_t3_resp_allKeys):
                t3_resp.keys = _t3_resp_allKeys[-1].name  # just the last key pressed
                t3_resp.rt = _t3_resp_allKeys[-1].rt
                # was this correct?
                if (t3_resp.keys == str(CorrAnsLoc)) or (t3_resp.keys == CorrAnsLoc):
                    t3_resp.corr = 1
                else:
                    t3_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial3"-------
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if t3_resp.keys in ['', [], None]:  # No response was made
        t3_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAnsLoc).lower() == 'none':
           t3_resp.corr = 1;  # correct non-response
        else:
           t3_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for t3_trials (TrialHandler)
    t3_trials.addData('t3_resp.keys',t3_resp.keys)
    t3_trials.addData('t3_resp.corr', t3_resp.corr)
    if t3_resp.keys != None:  # we had a response
        t3_trials.addData('t3_resp.rt', t3_resp.rt)
    # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 't3_trials'


# ------Prepare to start Routine "break_3"-------
continueRoutine = True
# update component parameters for each repeat
b3_resp.keys = []
b3_resp.rt = []
_b3_resp_allKeys = []
# keep track of which components have finished
break_3Components = [b3_inst, b3_timeRemaining, b3_resp]
for thisComponent in break_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_3"-------
while continueRoutine:
    # get current time
    t = break_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    b3_time = int(maxBT - break_3Clock.getTime())
    
    # *b3_inst* updates
    if b3_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b3_inst.frameNStart = frameN  # exact frame index
        b3_inst.tStart = t  # local t and not account for scr refresh
        b3_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b3_inst, 'tStartRefresh')  # time at next scr refresh
        b3_inst.setAutoDraw(True)
    if b3_inst.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b3_inst.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b3_inst.tStop = t  # not accounting for scr refresh
            b3_inst.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b3_inst, 'tStopRefresh')  # time at next scr refresh
            b3_inst.setAutoDraw(False)
    
    # *b3_timeRemaining* updates
    if b3_timeRemaining.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b3_timeRemaining.frameNStart = frameN  # exact frame index
        b3_timeRemaining.tStart = t  # local t and not account for scr refresh
        b3_timeRemaining.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b3_timeRemaining, 'tStartRefresh')  # time at next scr refresh
        b3_timeRemaining.setAutoDraw(True)
    if b3_timeRemaining.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b3_timeRemaining.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b3_timeRemaining.tStop = t  # not accounting for scr refresh
            b3_timeRemaining.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b3_timeRemaining, 'tStopRefresh')  # time at next scr refresh
            b3_timeRemaining.setAutoDraw(False)
    if b3_timeRemaining.status == STARTED:  # only update if drawing
        b3_timeRemaining.setText('남은 시간: {time}'.format(time=b3_time), log=False)
    
    # *b3_resp* updates
    waitOnFlip = False
    if b3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        b3_resp.frameNStart = frameN  # exact frame index
        b3_resp.tStart = t  # local t and not account for scr refresh
        b3_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b3_resp, 'tStartRefresh')  # time at next scr refresh
        b3_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(b3_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(b3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if b3_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b3_resp.tStartRefresh + maxBT-frameTolerance:
            # keep track of stop time/frame for later
            b3_resp.tStop = t  # not accounting for scr refresh
            b3_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b3_resp, 'tStopRefresh')  # time at next scr refresh
            b3_resp.status = FINISHED
    if b3_resp.status == STARTED and not waitOnFlip:
        theseKeys = b3_resp.getKeys(keyList=['space'], waitRelease=False)
        _b3_resp_allKeys.extend(theseKeys)
        if len(_b3_resp_allKeys):
            b3_resp.keys = _b3_resp_allKeys[-1].name  # just the last key pressed
            b3_resp.rt = _b3_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_3"-------
for thisComponent in break_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "break_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endM_resp.keys = []
endM_resp.rt = []
_endM_resp_allKeys = []
# keep track of which components have finished
endComponents = [endM, endM_resp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endM* updates
    if endM.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endM.frameNStart = frameN  # exact frame index
        endM.tStart = t  # local t and not account for scr refresh
        endM.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endM, 'tStartRefresh')  # time at next scr refresh
        endM.setAutoDraw(True)
    
    # *endM_resp* updates
    waitOnFlip = False
    if endM_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endM_resp.frameNStart = frameN  # exact frame index
        endM_resp.tStart = t  # local t and not account for scr refresh
        endM_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endM_resp, 'tStartRefresh')  # time at next scr refresh
        endM_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endM_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endM_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endM_resp.status == STARTED and not waitOnFlip:
        theseKeys = endM_resp.getKeys(keyList=['q'], waitRelease=False)
        _endM_resp_allKeys.extend(theseKeys)
        if len(_endM_resp_allKeys):
            endM_resp.keys = _endM_resp_allKeys[-1].name  # just the last key pressed
            endM_resp.rt = _endM_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
