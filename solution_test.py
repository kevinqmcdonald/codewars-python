import codewars_test as test
from solution import add


@test.describe('Fixed Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        test.assert_equals(add(1, 1), 2, 'Optional Message on Failure')

    @test.it("More tests")
    def more():
        for a, b, exp in [(-2, 30, 28), (42, 0, 42)]:
            test.assert_equals(add(a, b), exp)

    @test.it("Reduced group")
    def more():
        for v in range(10):
            test.assert_equals(add(v, v), 2 * v)


@test.describe('Random Tests')
def rnd_tests():
    pass
