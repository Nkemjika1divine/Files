#!/usr/bin/python3
"""Test for Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestForSquare(unittest.TestCase):
    
    def test_if_Square_is_base(self):
        """checks if Square is an instance of Base"""
        self.assertIsInstance(Square(2, 3), Base)
    
    def test_if_Square_is_Square(self):
        """checks if Square object is an instance of Square"""
        self.assertIsInstance(Square(2, 3), Square)
    
    def test_Square_for_args(self):
        """If Square has no args"""
        with self.assertRaises(TypeError):
            Square()
        
    def test_Square_for_args(self):
        """if recangle has one arg"""
        with self.assertRaises(TypeError):
            Square(10)
    
    def test_Square_size(self):
        """Check value for size"""
        r1 = Square(4, 5)
        self.assertEqual(r1.size, 4)
    
    def test_Square_x_no_args(self):
        """check value for x with no args"""
        r1 = Square(4)
        self.assertEqual(r1.x, 0)
    
    def test_Square_y_no_args(self):
        """check value for y without""" 
        r1 = Square(4)
        self.assertEqual(r1.y, 0)
    
    def test_Square_id_no_args(self):
        """check id with no args"""
        r1 = Square(4)
        self.assertEqual(r1.id, 1)
    
    def test_Square_x_with_args(self):
        """check value of x with args"""
        r1 = Square(4, 7)
        self.assertEqual(r1.x, 7)
    
    def test_Square_y_with_args(self):
        """check value for y with args"""
        r1 = Square(4, 5, 10)
        self.assertEqual(r1.y, 10)
    
    def test_Square_size_String(self):
        """check value of size with string"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square("String", 8, 10)
    
    def test_Square_size_None(self):
        """check if none is passed to size"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(None, 8, 10)
    
    def test_Square_size_float(self):
        """check if the value of size is float"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(5.7, 8, 10)
    
    def test_Square_size_bool(self):
        """check what happens when size is bool"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(True, 8, 10)
    
    def test_Square_x_String(self):
        """check value of x with string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, "bounce", 10)
    
    def test_Square_x_None(self):
        """check value of x with None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, None, 10)
    
    def test_Square_x_float(self):
        """check value of x with float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, 7.3, 10)
    
    def test_Square_x_bool(self):
        """check value of x with bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, True, 10)
    
    def test_Square_y_bool(self):
        """check value of y with bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 7, True)
    
    def test_Square_y_bool(self):
        """check value of y with bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 7, True)
    
    def test_Square_y_string(self):
        """check value of x with string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 7, "ac")
    
    def test_Square_y_float(self):
        """check value of x with float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 7, 7.3)
    
    def test_Square_size_negative(self):
        """check value of height with negative value"""
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            Square(-7, 6, 10)
    
    def test_Square_size_list(self):
        """check what happens when size is list"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square([6, 5], 5, 10)
    
    def test_Square_size_tuple(self):
        """check what happens when size is tuple"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square((3, 4), 5, 8, 10)
    
    def test_Square_size_dict(self):
        """check what happens when size is dictionary"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square({1: "bool"}, 5, 8, 10)
    
    def test_Square_size_set(self):
        """check what happens when size is set"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square({6, 9}, 5, 8, 10)
    
    def test_Square_size_complex(self):
        """check what happens when size is complex"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(complex(2), 5, 8, 10)
    
    def test_Square_size_nan(self):
        """check what happens when size is nan"""
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            Square(float('nan'), 5, 8, 10)
    
    def test_Square_x_list(self):
        """check what happens when size is list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, 7, [6, 5], 10)
    
    def test_Square_x_tuple(self):
        """check what happens when size is tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, (3, 4), 10)
    
    def test_Square_x_dict(self):
        """check what happens when size is dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {1: "bool"}, 10)
    
    def test_Square_x_set(self):
        """check what happens when size is set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, {6, 9}, 10)
    
    def test_Square_x_complex(self):
        """check what happens when size is complex"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, complex(2), 10)
    
    def test_Square_x_nan(self):
        """check what happens when size is nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(6, float('nan'), 10)

    def test_Square_y_list(self):
        """check what happens when size is list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 5, [6, 5])
    
    def test_Square_y_tuple(self):
        """check what happens when size is tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 4, (3, 4))
    
    def test_Square_y_dict(self):
        """check what happens when size is dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 5, {1: "bool"})
    
    def test_Square_y_set(self):
        """check what happens when size is set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, {6, 9})
    
    def test_Square_y_complex(self):
        """check what happens when size is complex"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 7, complex(2))
    
    def test_Square_y_nan(self):
        """check what happens when size is nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(6, 4, float('nan'))
    
    def test_Square_x_negative(self):
        """check value of x with negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(7, -1, 10)
    
    def test_Square_y_negative(self):
        """check value of y with negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(6, 6, -6)
    
    def test_Square_private_size(self):
        """check if size is private"""
        with self.assertRaises(AttributeError):
            print(Square(7, 6, 6, 10).__size)
    
    def test_Square_private_x(self):
        """check if x is private"""
        with self.assertRaises(AttributeError):
            print(Square(7, 6, 6, 10).__x)
    
    def test_Square_private_size(self):
        """check if y is private"""
        with self.assertRaises(AttributeError):
            print(Square(7, 6, 6, 10).__y)
    
    def test_Square_id_with_args(self):
        """check if id reflects if publicly assigned"""
        r1 = Square(4, 5, 3, 67)
        self.assertEqual(r1.id, 67)
    
    def test_Square_id_with_args(self):
        """check if id correlates"""
        r1 = Square(4, 5, 3, 67)
        r2 = Square(4, 5, 7)
        self.assertEqual(r1.id - 66, r2.id)
    
    def test_Square_id_init_assignment(self):
        """check if id automatically updates"""
        r1 = Square(2, 3, 8)
        r2 = Square(3, 4, 8)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_more_than_4_args(self):
        """check what happens when more than 4 args are passed"""
        with self.assertRaises(TypeError):
            Square(3, 4, 6, 7, 9)
    
    def test_Square_id_public_assign(self):
        """Check if id can be publicly assigned"""
        r1 =Square(2, 3, 7)
        r1.id = 100
        self.assertEqual(r1.id, 100)
    
    def test_Square_area(self):
        """check what area method returns"""
        r1 = Square(4)
        self.assertEqual(r1.area(), 16)
    
    def test_Square_area_large_num(self):
        """checks area for large number"""
        r1 = Square(99999)
        self.assertEqual(9999800001, r1.area())
    
    
    
    def test_Square_str_method_print_size(self):
        r = Square(4)
        capture = TestSquare_stdout.capture_stdout(r, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_Square_str_method_size_x(self):
        r = Square(5, 1)
        correct = "[Square] ({}) 1/0 - 5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_Square_str_method_size_x_y(self):
        r = Square(1, 2, 4)
        correct = "[Square] ({}) 2/4 - 1".format(r.id)
        self.assertEqual(correct, str(r))

    def test_Square_str_method_size_x_y_id(self):
        r = Square(13, 2, 4, 7)
        self.assertEqual("[Square] (7) 2/4 - 13", str(r))

    def test_Square_str_method_changed_attributes(self):
        r = Square(7, 0, 0, [4])
        r.size = 15
        r.x = 8
        r.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(r))

    def test_Square_str_method_one_arg(self):
        r = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.__str__(1)
    
    def test_Square_to_dictionary_output(self):
        r = Square(89, 1, 2, 6)
        output = {'x': 1, 'y': 2, 'id': 6, 'size': 89}
        self.assertDictEqual(r.to_dictionary(), output)
        
        
        
        
        
        
        
        
    def test_Square_update_no_args(self):
        """check update method with no arg"""
        r = Square(1, 1, 1, 1, )
        r.update()
        self.assertEqual("[Square] (1) 1/1 - 1", str(r))

    def test_Square_update_one_args(self):
        """check update method with one arg"""
        r = Square(1, 1, 1, 1, )
        r.update(8)
        self.assertEqual("[Square] (8) 1/1 - 1", str(r))

    def test_Square_update_two_args(self):
        """check update method with two arg"""
        r = Square(1, 1, 1, 1)
        r.update(8, 2)
        self.assertEqual("[Square] (8) 1/1 - 2", str(r))

    def test_Square_update_three_args(self):
        """check update method with four arg"""
        r = Square(1, 1, 1, 1)
        r.update(8, 3, 77)
        self.assertEqual("[Square] (8) 77/1 - 3", str(r))

    def test_Square_update_four_args(self):
        """check update method with five arg"""
        r = Square(1, 1, 1, 1)
        r.update(8, 2, 77, 10)
        self.assertEqual("[Square] (8) 77/10 - 2", str(r))

    def test_Square_update_more_four_args(self):
        """check update method with more than five arg"""
        r = Square(1, 1, 1, 1)
        r.update(8, 2, 77, 10, 6)
        self.assertEqual("[Square] (8) 77/10 - 2", str(r))

    def test_Square_update_args_None_id(self):
        """passing none to id via update method"""
        r = Square(1, 1, 1, 1)
        r.update(None)
        output = "[Square] ({}) 1/1 - 1".format(r.id)
        self.assertEqual(output, str(r))

    def test_Square_update_args_None_and_more(self):
        """test update with None id and more args"""
        r = Square(1, 1, 1, 1)
        r.update(None, 4, 2)
        output = "[Square] ({}) 2/1 - 4".format(r.id)
        self.assertEqual(output, str(r))

    def test_Square_update_args_str_size_(self):
        """update size with str"""
        r = Square(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "size must be an integer"):
            r.update(8, "i")

    def test_Square_update_args_size_zero(self):
        """test for updating size with 0"""
        r = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            r.update(9, 0)

    def test_Square_update_args_size_negative(self):
        """test for updating args with -ve value"""
        r = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "size must be > 0"):
            r.update(9, -7)

    def test_Square_update_args_x_str(self):
        """test for str bring passed to x via uodate method"""
        r = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, "invalid")

    def test_Square_update_args_x_negative(self):
        """update x wirh negative value"""
        r = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 2, -6)

    def test_Square_update_args_y_str(self):
        """Update y with str"""
        r = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 4, "invalid")

    def test_Square_update_args_y_negative(self):
        """uodate y with negative value"""
        r = Square(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 3, -6)

    
        
        
        
        


    @staticmethod
    def capture_stdout(sq, method):
        """Shows what is returned to stdout
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        s = Square(4)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test display method
    def test_display_size(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)

if __name__ == '__main__':
    unittest.main()
