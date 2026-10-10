import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from services.student_service import StudentService  # noqa: E402

DATA = {"name": "Ana", "email": "ana@example.com", "course": "BSIT", "year_level": "2"}


def make(tmp_path):
    return StudentService(str(tmp_path / "students.json"))


def test_add_and_get(tmp_path):
    svc = make(tmp_path)
    s = svc.add_student(DATA)
    assert svc.get_student(s["student_id"])["name"] == "Ana"
    assert len(svc.get_all_students()) == 1


def test_update(tmp_path):
    svc = make(tmp_path)
    s = svc.add_student(DATA)
    updated = svc.update_student(s["student_id"], {"course": "BSCS"})
    assert updated["course"] == "BSCS"
    assert svc.update_student("nope", {}) is None


def test_delete(tmp_path):
    svc = make(tmp_path)
    s = svc.add_student(DATA)
    assert svc.delete_student(s["student_id"]) is True
    assert svc.delete_student(s["student_id"]) is False
    assert svc.get_all_students() == []
