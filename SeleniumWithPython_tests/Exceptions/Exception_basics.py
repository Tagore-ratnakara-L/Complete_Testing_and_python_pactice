
ItemsInCart =0
#2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Products cart count is not matching")
#Exception: Products cart count is not matching
    pass

#assert (ItemsInCart == 2) #AssertionError
assert (ItemsInCart == 0) #No error generated since we are paasing it using assertion

#try , catch mechanism
#wrap test case in try block that it intends to fail
#let code continue in catch block to perform remaining cases

# try:
#     with open('filelog.txt','r') as reader:
#         reader.read()
# except:
#     print("somehow i raised this block because of failure in try block.")
#     #somehow i raised this block because of failure in try block.
#
# #perfect code
# try:
#     with open('text.txt','r') as reader:
#         reader.read()
# except:
#     print("somehow i raised this block because of failure in try block.")
#     # this reads perfectly

#catch the error python throws in to e
try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e) #[Errno 2] No such file or directory: 'filelog.txt'
    # this pass the test but behind caught error
#key word finally is runs no matter if test fails or pass in try , catch mechanism
finally:
    print("Cleaning up resources")# Cleaning up resources
    # code has n munber of lines and fails in middle or pass but comes to finally and executes