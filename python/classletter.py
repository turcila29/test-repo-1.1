class lettertests:

        def testletter(self,inputstringofletter):
                self.stringofletter = inputstringofletter

        def testletter(self,inputletter):
                if inputletter in self.stringofletter:
                    return True
                else:
                        return False
                


                horizsymm = lettertests('BCDEHIKOX')
                vertsymm = lettertests('AHIMOTUVWXY')
                horizvertsym = lettertests('HIOX')
                rotsymm = lettertests('HINOSXZ')

                userletter =''

                while userletter != 0:
                       userletter = input('enter a single character, 0 to quit: ')
                       print("Horiz Symm " + horizsymm.testletter(userletter))
                       print("vertsymm " + horizsymm.testletter(userletter))
                       print("horizvertsym " + horizsymm.testletter(userletter))
                       print("rotsymm " + horizsymm.testletter(userletter))