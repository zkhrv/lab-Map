from Map import Map

class TestMap:
    @staticmethod
    def main():
        test_map = Map()
        test_map.add_element(3, "Addel")
        test_map.add_element(5, "Back")
        test_map.add_element(1, "Lily")
        test_map.add_element(9, "Janny")
        test_map.add_element(8, "Sam")
        test_map.add_element(2, "Madam")
        test_map.add_element(6, "Jerry")
        test_map.add_element(10, "Rodger")
        
        copy_map = Map(test_map)
        copy_map.change_element(2, "Sir")
        copy_el = copy_map.get_element_node(2)
        orig_el = test_map.get_element_node(2)
        if copy_el is not None and orig_el is not None:
            print("-----------------------------------------------------------")
            print("В оригинале под ключом", orig_el.key, "хранится значение:", orig_el.data)
            print("А в копии под этим же ключом уже:", copy_el.data)
            print("-----------------------------------------------------------")
        copy_map.clear()
        print("-----------------------------------------------------------")

TestMap.main()