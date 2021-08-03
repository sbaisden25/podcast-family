Getting Started
===============

- Right-click to access the menu. Several configuration options are available by selecting
  "Configure" from the menu.

- A safeguard is in place to prevent accidentally pressing the Split key multiple times. The
  sensitivity of this feature is adjustable (Menu -> Configure) and may be disabled.

- In the Run Editor (accessed via New/Edit) ...

	- Only the Segment Name is mandatory.
	- When inputting times directly from a video, you can directly enter the video
	  timestamps at each split, then after all times are entered, type the starting time
	  offset (the timestamp in the video when timing begins) in the "Old time offset"
	  box and click "Apply". The offset time will be subtracted from all times in the
	  "Old Time" column.
	- Icons may be set for each segment by double-clicking the icon field, or by selecting
	  one or more icon fields and pressing "Enter".
	- You can import files from other known split timers (Only Llanfair is supported so far)

- About personal bests ...

	Two methods of tracking personal bests are available from the menu:

	- The default mode, "Fastest overall run", will record all split times from any run
	  that beats your previous best. In this mode, the personal best time recorded for
	  each segment will match the time in your best complete run.
	- Alternatively, "Fastest to each split" will keep track of your personal best time
	  reaching each split. In this mode, a personal best time for any given segment will
	  be the fastest you have ever gotten that far in the run.

	- Pressing Reset (R) will reset the timer prompting you to update your personal bests or
	  not. This can be used even at the end of a run while the final time is displayed.

	- If personal best times are updated by mistake (for example, if you held down the
	  split hotkey, or just pressed it too many times) you can use Reload from the menu
	  to restore saved data from the time file.

- At the end of a run before resetting the timer, you can manually save the splits by using
  "Set this run as old" from the menu. This may be useful if you want to keep a run's splits
  while using the "Fastest to each split" personal best tracking mode, or want to keep a run
  to compare against even if it is not your best.

- Use "Start Delay" from the configure window to set a delayed start time. The delay can be
  precise to milliseconds.
  
- A "Start At..." option have been made available to start the timer at a given offset. This
  allow you to start the timer back at a said point after a system crash or to compare to
  splits during practice more efficiently. Of course, it's not limited to those cases.

- Global hotkeys may be configured for all timer functions (Menu -> Configure). This
  allows you to use timer functions without the timer being "in focus" in Windows.

- If you wish to see more information than is displayed in the "detailed" display mode, you
  may pop up an extra "advanced detail" window that can display additional information. The
  information displayed in this window can be configured by right-clicking the window*, and
  the number of segments displayed can be configured in the same manner as the detailed mode.
  This window will only display when segment data has been loaded or created.
   *note - if you select to show segment times, the segment time (in square brackets)
    displayed under "Best [Seg]" will be the fastest recorded time for that segment (this
    is the "Best Seg" data in the Run Editor)

Hotkeys
=======

S		Stop

R		Reset (same as Stop, but does not save any new best times)

P		Pause, Resume

Space/Enter	Play/Resume, Split (or Pause if no run info is loaded)

Left/Right	Previous/Next segments
		(works mid-run if you miss a split or accidentally hit split twice, even on
                the finished screen)

Up/Down		Increases/Decreases the number of segments displayed in the detailed display
		mode (may be between 2 and 40)

0-3		Change the display mode (when no run is present, timer only mode is forced)

		0 - Timer only: only the timer is displayed
		1 - Compact: current segment data is shown above and below the timer
		2 - Wide: current segment data is shown to the right of the timer
		3 - Detailed: extended segment data is shown above the timer (the number of
			segments displayed can be adjusted via the menu or Up/Down arrow keys)

Credit
======

The digital clock font embedded is "DIGITAL-7" by Sizenko Alexander.
http://www.styleseven.com

Contact
=======

Original timer has been created by Wodanaz @SDA. Updates upwards from 1.5.0 have been
made by Nitrofski. If you wish to contact me, use one of the following:
Twitch: twitch.tv/Nitrofski
Twitter: @Nitrofski or #WSplit