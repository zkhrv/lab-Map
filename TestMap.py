from Map import Map

class TestMap:
    @staticmethod
    def main():
        test_map = Map()
    
        test_map.AddEl(3, "Addel")
        test_map.AddEl(5, "Back")
        test_map.AddEl(1, "Lily")
        test_map.AddEl(9, "Janny")
        test_map.AddEl(8, "Sam")
        test_map.AddEl(2, "Madam")
        test_map.AddEl(6, "Jerry")
        test_map.AddEl(10, "Rodger")
        
        copy_map = test_map
        copy_map.ChangeEl(2, "Sir")
        copy_el = copy_map.ElemetnPoinet(2)
        orig_el = test_map.ElemetnPoinet(2)
        if copy_el is not None and orig_el is not None:
            print("-----------------------------------------------------------")
            print("В оригинале под ключом " + str(orig_el.key) + " хранится значение: " + orig_el.data)
            print("А в копии по этим же ключом уже: " + copy_el.data)
            print("-----------------------------------------------------------")
        copy_map.clear()
        print("-----------------------------------------------------------")

TestMap.main()
