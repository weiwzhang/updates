# Report for Alvin Zhang

*This report combines 1 individual submissions.*

#Past
- Implement travis-CI
 - Add nosetests with coverage module
 - Add tests for feature extractors
 - Remove tests where we test our results against another library's results using large music files.
 - Create test signals - ones, sinusoid, sawtooth, and strictly alternating.
 - Add tests for RMS, ZCR, and spectral centroid based on these test signals. Test both framewise and single-window.
- Clean up extractor and utils files
 - Clean up documentation for RMS, ZCR, and spectral centroid.
 - Change pad/padAmt variable to pad consistently.
 - Add assertions for y, win_length, hop_length, and pad.
 - Change framewise to not use librosa functions, use list comprehension, and dynamically pad both sides by reflection.
 - Add spectrogram utility to utils.py, now using np.fft.rfft and creating a threshold at 1% of the maximum frequency's amiplitude.
#Future
- Continue writing tests
 - Spectral spread, spectral flatness, fluctuation entropy, fluctuation centroid, key clarity, and pulse clarity are the next features to review the algorithms and rewrite the tests for.

