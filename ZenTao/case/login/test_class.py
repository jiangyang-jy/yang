import pytest
class TestClass:
    def test_one(self):
        x = 'this'
        print('学习pytest')
        assert 'h' in x

    def test_two(self):
        z = "jiang"
        assert hasattr(z, "jiang")

if __name__ == '__main__':
    pytest.main(["-s", "test_class.py"])
