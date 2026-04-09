import inspect
import list_practice as list_practice


def test_header_comments():
    """Test that the module docstring contains required header fields: author and date."""
    source = inspect.getsource(list_practice)

    assert "author:" in source, "Missing 'author:' in header comments"
    assert "date:" in source, "Missing 'date:' in header comments"


def test_roll_dice_docstring():
    """Test that roll_dice() has a completed docstring (not just TODO)."""
    docstring = list_practice.roll_dice.__doc__
    assert docstring is not None, "roll_dice() is missing a docstring"
    assert "TODO" not in docstring, "roll_dice() docstring still contains TODO"
    assert len(docstring.strip()) > 20, "roll_dice() docstring is too short"
    assert "return" in docstring.lower(), "roll_dice() docstring should describe what it returns"


def test_count_john_basic():
    """Test count_john() returns correct percentage with a mix of names."""
    assert list_practice.count_john(["sara", "abc", "john"]) == 33.3


def test_count_john_multiple():
    """Test count_john() returns correct percentage with multiple johns."""
    assert list_practice.count_john(["john", "mark", "henry", "john", "john", "barbara"]) == 50.0


def test_count_john_no_johns():
    """Test count_john() returns 0.0 when no johns are in the list."""
    assert list_practice.count_john(["alice", "bob", "charlie"]) == 0.0


def test_count_john_all_johns():
    """Test count_john() returns 100.0 when all names are john."""
    assert list_practice.count_john(["john", "john", "john"]) == 100.0


def test_count_john_empty():
    """Test count_john() returns 0.0 for an empty list."""
    assert list_practice.count_john([]) == 0.0


def test_roll_dice_returns_float(monkeypatch):
    """Test that roll_dice() returns a float."""
    # Force dice rolls: 3, 5, 6 -> average of (3+5+6)/3 = 4.7
    rolls = iter([3, 5, 6])
    monkeypatch.setattr("random.randint", lambda a, b: next(rolls))

    result = list_practice.roll_dice()

    assert isinstance(result, float), f"Expected float, got {type(result)}"


def test_roll_dice_correct_average(monkeypatch):
    """Test that roll_dice() returns the correct rounded average."""
    # Force dice rolls: 3, 5, 6 -> average of (3+5+6)/3 = 4.7
    rolls = iter([3, 5, 6])
    monkeypatch.setattr("random.randint", lambda a, b: next(rolls))

    result = list_practice.roll_dice()

    assert result == 4.7, f"Expected 4.7, got {result}"


def test_roll_dice_stops_on_six(monkeypatch, capsys):
    """Test that roll_dice() stops rolling once a 6 is rolled."""
    # Force rolls: 2, 6 — should stop after the 6
    rolls = iter([2, 6])
    monkeypatch.setattr("random.randint", lambda a, b: next(rolls))

    list_practice.roll_dice()
    captured = capsys.readouterr()

    assert "You rolled a: 2" in captured.out
    assert "You rolled a: 6" in captured.out


def test_roll_dice_first_roll_six(monkeypatch):
    """Test that roll_dice() handles rolling a 6 on the first try."""
    monkeypatch.setattr("random.randint", lambda a, b: 6)

    result = list_practice.roll_dice()

    assert result == 6.0, f"Expected 6.0, got {result}"
