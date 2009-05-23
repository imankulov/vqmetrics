Voice quality metrics
-----------------------

Python module which contains a set of functions to convert between different
speech quality estimation metrics such as PESQ MOS, MOS LQO, R-factor.

Contains also one helper class with Speex codec options:

  - mapping between speex "quality" and "mode" option
  - size (in bits) for earch speex frame with given mode
  - required bandwidth estimation

Terminology
-------------

According to [P.800.1][1] ITU-T Recommendation, there is different "subtypes"
of mean opinion score.

Recommendation states:

<cite>
The following identifiers are recommended to be used together with the
abbreviation MOS in order to distinguish the area of application, where "LQ"
refers to Listening Quality, "CQ" refers to Conversational Quality, "S" refers to
Subjective, "O" refers to Objective, and "E" refers to Estimated.
</cite>

Thus, there are six abbreviations:

<table>
<tr>
	<th></th><th>Listening-only</th><th>Conversational</th>
</tr>
<tr>
	<td>Subjective</td><td>MOS-LQS</td><td>MOS-CQS</td>
</tr>
<tr>
	<td>Objective</td><td>MOS-LQO</td><td>MOS-CQO</td>
</tr>
<tr>
	<td>Estimated</td><td>MOS-LQE</td><td>MOS-CQE</td>
</tr>
</table>

[E-model][2] estimaton returns MOS-LQE without delay and echo impairments
calculation and  MOS-CQE with these impairments taken into account.

[PESQ][3] estimation returns value which can be converted to MOS-LQO.


[1]: http://www.itu.int/rec/T-REC-P.800.1/en "P.800.1. Mean Opinion Score (MOS) terminology"
[2]: http://www.itu.int/rec/T-REC-G.107/en "G.107. The E-model: a computational model for use in transmission planning"
[3]: http://www.itu.int/rec/T-REC-P.862/en "P.862. Perceptual evaluation of speech quality (PESQ)"
