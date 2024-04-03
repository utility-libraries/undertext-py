# Notes

| Format                                  | suffix |             |
|-----------------------------------------|--------|-------------|
| [WebVTT](#webvtt)                       | `.vtt` |             |
| [SubViewer](#subviewer)                 | `.sbv` |             |
| [SubRipper](#subrip)                    | `.srt` |             |
| [MicroDVD](#microdvd)                   | `.sub` |             |
| [Sub Station Alpha](#sub-station-alpha) | `.ssa` |             |

## WebVTT

```vtt
WEBVTT

00:11.000 --> 00:13.000
<v Roger Bingham>We are in New York City

00:13.000 --> 00:16.000
<v Roger Bingham>We're actually at the Lucern Hotel, just down the street

00:16.000 --> 00:18.000
<v Roger Bingham>from the American Museum of Natural History

00:18.000 --> 00:20.000
<v Roger Bingham>And with me is Neil deGrasse Tyson
```

## SubViewer

```sbv
0:00:01.000,0:00:03.000
Hello, and welcome to our video!

0:00:04.000,0:00:06.000
In this video, we will be discussing the SBV file format.

0:00:07.000,0:00:10.000
The SBV format is commonly used for storing subtitles for videos.[br]Also allows for newlines
```

## SubRip

```srt
1
00:02:16,612 --> 00:02:19,376
Senator, we're making
our final approach into Coruscant.

2
00:02:19,482 --> 00:02:21,609
Very good, Lieutenant.

3
00:03:13,336 --> 00:03:15,167
We made it.

4
00:03:18,608 --> 00:03:20,371
I guess I was wrong.

5
00:03:20,476 --> 00:03:22,671
There was no danger at all.
```

## MicroDVD

> [!CAUTION]
> Numbers are for frames and not seconds

```microdvd
{0}{100}Subtitle line 1
{150}{300}Subtitle line 2
{350}{550}Subtitle line 3
```

## Sub Station Alpha

> [!CAUTION]
> Different Versions are possible
> 
> - SSA V4+ (`.ass`)
> - SSA v4 (below)
> - SSA v3
> - SSA v1

```ssa
[Script Info]
; This is a Sub Station Alpha v4 script.
; For Sub Station Alpha info and downloads,
; go to http://www.eswat.demon.co.uk/
; or email kotus@eswat.demon.co.uk
Title: Spirited Away
Original Script: Ian Roberts
Original Translation: Eisuke Ishibashi
ScriptType: v4.00
Collisions: Normal
PlayResY: 480
PlayDepth: 0
Wav: 0, 28688,H:\3.wav
LastWav: 1
Timer: 100.0000

[V4 Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, TertiaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, AlphaLevel, Encoding
Style: ICredit,Gill Sans Condensed,36,16777215,65535,65535,-2147483640,-1,0,1,3,0,2,70,70,40,0,0
Style: IDefault,Gill Sans Condensed,30,65535,65535,65535,-2147483640,-1,0,1,3,0,2,70,70,40,0,0
Style: IScreenText,Gill Sans Condensed,30,16744576,65535,65535,-2147483640,-1,0,1,3,5,2,70,70,40,0,0

[Events]
Format: Marked, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: Marked=0,0:00:06.60,0:00:08.90,IScreenText,,0000,0000,0000,,{\a10}See you again... Best wishes
Dialogue: Marked=0,0:00:11.84,0:00:14.74,ICredit,,0000,0000,0100,,{\a2}Story, Script & Direction - MIYAZAKI Hayao
```
