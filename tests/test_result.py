from source.main import main


def test_result():
    main('tests/test_files/good.csv')

    with open('result') as res:
        lines = res.read().splitlines()

    assert lines[0] == 'Day 2019-02-04 Work 10:27:05 ot'
    assert lines[1] == 'Day 2019-02-05 Work 6:16:02 i'
    assert lines[2] == 'Day 2019-02-06 Work 6:47:47'
    assert lines[3] == 'Day 2019-02-07 Work 9:23:53 ot 32:54:47 0:54:47'

    assert len(lines) == 4
