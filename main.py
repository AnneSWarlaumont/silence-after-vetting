import xmltodict
import pprint
import parsing_functions
import os
with open('/users/curt/desktop/elan_test.eaf') as fd:
    doc = xmltodict.parse(fd.read())

'''
List of all TIERs, each one can be accessed by indexing followed by
keys() and values() function
'''
list_of_TIER_objs = doc['ANNOTATION_DOCUMENT']['TIER']

'''
List of all TIME_SLOTs, each can be accessed by indexing followed
by keys() and values() function
'''
list_of_TIME_SLOT_objs = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']

'''
Ask user for for name of TIER (e.g. cut, bookmark)
'''
user_input_tier_name = raw_input('Enter a tier name: ')

'''
all_TIER_ID_names contains a list of TIER_ID names
'''
all_TIER_ID_names = parsing_functions.get_unique_TIER_ID(list_of_TIER_objs)

# Maybe you can try and limit or make it more convenient for the user
#   by providing a list of tier names depending on the file they provide
# Or you can also provide an option for them to type it in
# for ex:
#   Enter a tier name or choose a number from the following selection:
#   1) cut
#   2) bookmark
#   0) exit

'''
This if-else statement checks the users input with list of all
  TIER_ID names

If the input is valid then the program will run
  else, an error message will appear providing a list of names
  of available TIERs
'''
if user_input_tier_name in all_TIER_ID_names:
    print("Process the results for [%s" %user_input_tier_name + "] tier")

    '''
    time_id_and_value_dict is a dictionary that contains
        the values of TIME_SLOT_ID and TIME_VALUE
    '''
    time_id_and_value_dict = parsing_functions.extract_TIME_ID_and_VALUE(list_of_TIME_SLOT_objs)

    '''
    tier_idx_number is the number associated with the TIER name
        prompted by the user
    '''
    tier_idx_number = all_TIER_ID_names.index(user_input_tier_name)

    '''
    list_of_ANNOTATIION_objs contains all ANNOTATIONS to a
        specific TIER
    '''
    list_of_ANNOTATIION_objs = list_of_TIER_objs[tier_idx_number]['ANNOTATION'] # maybe turn into function

    '''
    final_product is a nested dictionary containing all the ANNOTATION
        values
    '''
    final_product = parsing_functions.extract_ANNOTATION_values(list_of_ANNOTATIION_objs, time_id_and_value_dict)
    pprint.pprint(final_product)

    # save final_product to disk

else:
    parsing_functions.no_valid_results(all_TIER_ID_names)

print('annotation_id =',final_product['a11'])
print('start time =',final_product['a11']['start_cut_value'])
print('end time =',final_product['a11']['end_cut_value'])

# check if user input , then error message, these are the 4 available
#
# check user input with this list
# run code if it passes
# then get_TIER
# just a test change






























#
