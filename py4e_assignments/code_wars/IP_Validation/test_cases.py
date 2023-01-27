import codewars_test as test
from IP_Validation import is_valid_ip


@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(is_valid_ip('12.255.56.1'), True)
        test.assert_equals(is_valid_ip(''), False)
        test.assert_equals(is_valid_ip('abc.def.ghi.jkl'), False)
        test.assert_equals(is_valid_ip('123.456.789.0'), False)
        test.assert_equals(is_valid_ip('12.34.56'), False)
        test.assert_equals(is_valid_ip('12.34.56 .1'), False)
        test.assert_equals(is_valid_ip('12.34.56.-1'), False)
        test.assert_equals(is_valid_ip('123.045.067.089'), False)
        test.assert_equals(is_valid_ip('127.1.1.0'), True)
        test.assert_equals(is_valid_ip('0.0.0.0'), True)
        test.assert_equals(is_valid_ip('0.34.82.53'), True)
        test.assert_equals(is_valid_ip('192.168.1.300'), False)
