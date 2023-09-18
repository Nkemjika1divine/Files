#!/usr/bin/python3
"""Test for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestForRectangle(unittest.TestCase):
    
    def test_if_rectangle_is_base(self):
        """checks if Rectangle is an instance of Base"""
        self.assertIsInstance(Rectangle(2, 3), Base)
    
    def test_if_rectangle_is_Rectangle(self):
        """checks if Rectangle object is an instance of Rectangle"""
        self.assertIsInstance(Rectangle(2, 3), Rectangle)

    def test_rectangle_for_args(self):
        """If rectangle has no args"""
        with self.assertRaises(TypeError):
            Rectangle()
        
    def test_rectangle_for_args(self):
        """if recangle has one arg"""
        with self.assertRaises(TypeError):
            Rectangle(10)
    
    def test_rectangle_width(self):
        """Check value for width"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.width, 4)
    
    def test_rectangle_height(self):
        """check value for height"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.height, 5)
    
    def test_rectangle_x_no_args(self):
        """check value for x with no args"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.x, 0)
    
    def test_rectangle_y_no_args(self):
        """check value for y without""" 
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.y, 0)
    
    def test_rectangle_id_no_args(self):
        """check id with no args"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.id, 1)
    
    def test_rectangle_x_with_args(self):
        """check value of x with args"""
        r1 = Rectangle(4, 5, 7)
        self.assertEqual(r1.x, 7)
    
    def test_rectangle_y_with_args(self):
        """check value for y with args"""
        r1 = Rectangle(4, 5, 8, 10)
        self.assertEqual(r1.y, 10)
    
    def test_rectangle_width_String(self):
        """check value of width with string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("String", 5, 8, 10)
    
    def test_rectangle_width_None(self):
        """check if none is passed to width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5, 8, 10)
    
    def test_rectangle_width_float(self):
        """check if the value of width is float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.7, 5, 8, 10)
    
    def test_rectangle_width_bool(self):
        """check what happens when width is bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5, 8, 10)
    
    def test_rectangle_height_String(self):
        """check value of height with string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, "string", 8, 10)
    
    def test_rectangle_height_bool(self):
        """check value of height with bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, True, 8, 10)
    
    def test_rectangle_height_None(self):
        """check value of height with None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, None, 8, 10)
    
    def test_rectangle_height_float(self):
        """check value of height with float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, 7.8, 8, 10)
    
    def test_rectangle_x_String(self):
        """check value of x with string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 6, "bounce", 10)
    
    def test_rectangle_x_None(self):
        """check value of x with None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 6, None, 10)
    
    def test_rectangle_x_float(self):
        """check value of x with float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 6, 7.3, 10)
    
    def test_rectangle_x_bool(self):
        """check value of x with bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 6, True, 10)
    
    def test_rectangle_y_bool(self):
        """check value of x with bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 6, 7, True)
    
    def test_rectangle_y_bool(self):
        """check value of x with bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 6, 7, True)
    
    def test_rectangle_y_string(self):
        """check value of x with string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 6, 7, "ac")
    
    def test_rectangle_y_float(self):
        """check value of x with float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 6, 7, 7.3)
    
    def test_rectangle_width_negative(self):
        """check value of height with negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-7, 6, 6, 10)
    
    def test_rectangle_height_negative(self):
        """check value of height with negative value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(7, -6, 6, 10)
    
    def test_rectangle_width_list(self):
        """check what happens when width is list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([6, 5], 5, 8, 10)
    
    def test_rectangle_width_tuple(self):
        """check what happens when width is tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, 4), 5, 8, 10)
    
    def test_rectangle_width_dict(self):
        """check what happens when width is dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1: "bool"}, 5, 8, 10)
    
    def test_rectangle_width_set(self):
        """check what happens when width is set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({6, 9}, 5, 8, 10)
    
    def test_rectangle_width_complex(self):
        """check what happens when width is complex"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 5, 8, 10)
    
    def test_rectangle_width_nan(self):
        """check what happens when width is nan"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 5, 8, 10)

    def test_rectangle_height_list(self):
        """check what happens when width is list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, [6, 5], 8, 10)
    
    def test_rectangle_height_tuple(self):
        """check what happens when width is tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, (3, 4), 8, 10)
    
    def test_rectangle_height_dict(self):
        """check what happens when width is dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {1: "bool"}, 8, 10)
    
    def test_rectangle_height_set(self):
        """check what happens when width is set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, {6, 9}, 8, 10)
    
    def test_rectangle_height_complex(self):
        """check what happens when width is complex"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, complex(2), 8, 10)
    
    def test_rectangle_height_nan(self):
        """check what happens when width is nan"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, float('nan'), 8, 10)
    
    def test_rectangle_x_list(self):
        """check what happens when width is list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 7, [6, 5], 10)
    
    def test_rectangle_x_tuple(self):
        """check what happens when width is tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 8, (3, 4), 10)
    
    def test_rectangle_x_dict(self):
        """check what happens when width is dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 6, {1: "bool"}, 10)
    
    def test_rectangle_x_set(self):
        """check what happens when width is set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 5, {6, 9}, 10)
    
    def test_rectangle_x_complex(self):
        """check what happens when width is complex"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, complex(2), 10)
    
    def test_rectangle_x_nan(self):
        """check what happens when width is nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 4, float('nan'), 10)

    def test_rectangle_y_list(self):
        """check what happens when width is list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 7, 5, [6, 5])
    
    def test_rectangle_y_tuple(self):
        """check what happens when width is tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 8, 4, (3, 4))
    
    def test_rectangle_y_dict(self):
        """check what happens when width is dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 5, {1: "bool"})
    
    def test_rectangle_y_set(self):
        """check what happens when width is set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 5, 6, {6, 9})
    
    def test_rectangle_y_complex(self):
        """check what happens when width is complex"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 8, 7, complex(2))
    
    def test_rectangle_y_nan(self):
        """check what happens when width is nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(6, 4, 8, float('nan'))
    
    def test_rectangle_x_negative(self):
        """check value of x with negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(7, 6, -1, 10)
    
    def test_rectangle_y_negative(self):
        """check value of y with negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 6, 6, -6)
    
    def test_rectangle_private_width(self):
        """check if width is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 6, 6, 10).__width)
    
    def test_rectangle_private_height(self):
        """check if height is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 6, 6, 10).__height)
    
    def test_rectangle_private_x(self):
        """check if x is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 6, 6, 10).__x)
    
    def test_rectangle_private_width(self):
        """check if y is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 6, 6, 10).__y)
    
    def test_rectangle_id_with_args(self):
        """check if id reflects if publicly assigned"""
        r1 = Rectangle(4, 5, 7, 3, 67)
        self.assertEqual(r1.id, 67)
    
    def test_rectangle_id_with_args(self):
        """check if id correlates"""
        r1 = Rectangle(4, 5, 7, 3, 67)
        r2 = Rectangle(4, 5, 7, 3)
        self.assertEqual(r1.id - 66, r2.id)
    
    def test_rectangle_id_init_assignment(self):
        """check if id automatically updates"""
        r1 = Rectangle(2, 3, 7, 8)
        r2 = Rectangle(3, 4, 7, 8)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_more_than_5_args(self):
        """check what happens when more than 5 args are passed"""
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 6, 7, 9, 1)
    
    def test_rectangle_id_public_assign(self):
        """Check if id can be publicly assigned"""
        r1 =Rectangle(2, 3, 7, 8)
        r1.id = 100
        self.assertEqual(r1.id, 100)
    
    def test_rectangle_area(self):
        """check what area method returns"""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.area(), 20)
    
    def test_rectangle_area_large_num(self):
        """checks area for large number"""
        r1 = Rectangle(999999999999, 2)
        self.assertEqual(1,999,999,999,998, r1.area())
    
    
    
    def test_rectangle_str_method_print_width_height(self):
        """testing for str method with 2 args"""
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_rectangle_str_method_width_height_x(self):
        """testing for 3 args to str method"""
        r = Rectangle(5, 5, 1)
        update = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(update, r.__str__())

    def test_rectangle_str_method_width_height_x_y(self):
        """testing for 4 args to str method"""
        r = Rectangle(1, 8, 2, 4)
        output = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(output, str(r))

    def test_rectangle_str_method_width_height_x_y_id(self):
        """testing for all args to str method"""
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_rectangle_str_method_changed_attributes(self):
        """testing str method output"""
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_rectangle_str_method_one_arg(self):
        """testing for an arg"""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_rectangle_to_dictionary_output(self):
        """testing for dictionary output"""
        r = Rectangle(89, 7, 1, 2, 6)
        output = {'x': 1, 'y': 2, 'id': 6, 'height': 7, 'width': 89}
        self.assertDictEqual(r.to_dictionary(), output)
    
    def test_rectangle_update_copy_args(self):
        """test if two objects are the same if copied"""
        r1 = Rectangle(1, 2, 6, 9, 5)
        r2 = Rectangle(8, 8 1, 20, 30)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        """passing arg to the method"""
        r = Rectangle(19, 3, 4, 3, 4)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
    
    def test_rectangle_update_no_args(self):
        """check update method with no arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(r))

    def test_rectangle_update_one_args(self):
        """check update method with one arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(8)
        self.assertEqual("[Rectangle] (8) 1/1 - 1/1", str(r))

    def test_rectangle_update_two_args(self):
        """check update method with two arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(8, 2)
        self.assertEqual("[Rectangle] (8) 1/1 - 2/1", str(r))

    def test_rectangle_update_three_args(self):
        """check update method with three arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(8, 2, 3)
        self.assertEqual("[Rectangle] (8) 1/1 - 2/3", str(r))

    def test_rectangle_update_four_args(self):
        """check update method with four arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(8, 2, 3, 77)
        self.assertEqual("[Rectangle] (8) 77/1 - 2/3", str(r))

    def test_rectangle_update_five_args(self):
        """check update method with five arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(8, 2, 3, 77, 10)
        self.assertEqual("[Rectangle] (8) 77/10 - 2/3", str(r))

    def test_rectangle_update_more_five_args(self):
        """check update method with more than five arg"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(8, 2, 3, 77, 10, 6)
        self.assertEqual("[Rectangle] (8) 77/10 - 2/3", str(r))

    def test_rectangle_update_args_None_id(self):
        """passing none to id via update method"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(None)
        output = "[Rectangle] ({}) 1/1 - 1/1".format(r.id)
        self.assertEqual(output, str(r))

    def test_rectangle_update_args_None_and_more(self):
        """test update with None id and more args"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(None, 4, 5, 2)
        output = "[Rectangle] ({}) 2/1 - 4/5".format(r.id)
        self.assertEqual(output, str(r))

    def test_rectangle_update_args_str_width_(self):
        """update width with str"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(8, "i")

    def test_rectangle_update_args_width_zero(self):
        """test for updating width with 0"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(9, 0)

    def test_rectangle_update_args_width_negative(self):
        """test for updating args with -ve value"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(9, -7)

    def test_rectangle_update_args_str_height(self):
        """update height with str"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(8, 42, "i")

    def test_rectangle_update_args_height_zero(self):
        """pass 0 to height via uodate method"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(9, 1, 0)

    def test_rectangle_update_args_height_negative(self):
        """pass negative value to height via update method"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(9, 1, -5)

    def test_rectangle_update_args_str(self):
        """test for str bring passed to x via uodate method"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_rectangle_update_args_x_negative(self):
        """update x wirh negative value"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_rectangle_update_args_y_str(self):
        """Update y with str"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_rectangle_update_args_y_negative(self):
        """uodate y with negative value"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

if __name__ == '__main__':
    unittest.main()
