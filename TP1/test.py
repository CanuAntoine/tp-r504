import pytest
import fonctions as f

def test_1():
  assert f.puissance(2,3) == 8
  assert f.puissance(2,2) == 4

def test_2():
  assert f.puissance(-1,2) == 1
  assert f.puissance(-1,3) == -1
  assert f.puissance(-1,-1) == -1
  assert f.puissance(-1,-2) == 1
  assert f.puissance(-2,-1) == -0.5

def test_3():
  assert f.puissance(0,1) == 0
  assert f.puissance(0,10) == 0
  assert f.puissance(0,100) == 0
  assert f.puissance(0,1000) == 0

  assert f.puissance(0,0) == 1

  with pytest.raises(ValueError):
    assert f.puissance(0,-1)
    assert f.puissance(0,-10)
    assert f.puissance(0,-100)
    assert f.puissance(0,-1000)

  assert f.puissance(2, 1.2) == pytest.approx(2.29739671)
  assert f.puissance(2,-1.2) == pytest.approx(0.435275282)