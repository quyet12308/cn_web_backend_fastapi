# from fastai import APIRouter
# from base import random_number

# from check_database import get_max_id_from_table
# from home_screen_database import query_database_for_tourist_destination_information_by_id, query_database_for_type_file_img_by_id

# router_home = APIRouter()



# @router_home.get("/api/get_tourist_destination_information")
# async def get_tourist_destination_information():
#     tourist_destination_name_arr = []
#     img_base64_arr = []
#     price_arr = []
#     the_right_time_to_go_arr = []
#     tourist_destination_describe_arr = []
#     tourist_destination_location_arr = []
#     number_of_stars_arr = []
#     number_of_travel_days_arr = []
#     type_file_arr = []
#     for i in range(3):

#         max_id = get_max_id_from_table(path_of_database='database\\tourist_destination_information.db',table_name="type_of_file_img")
#         randum_num = random_number(end=max_id,start=1)
#         ttestdata =  query_database_for_tourist_destination_information_by_id(randum_num)
#         testdata2 = query_database_for_type_file_img_by_id(randum_num)
#         id_ , name_ , type_file_ = testdata2
#         id ,tourist_destination_name,img_base64,price,the_right_time_to_go,createdTime,tourist_destination_describe,tourist_destination_location,number_of_stars ,number_of_travel_days = ttestdata
        
#         tourist_destination_name_arr.append(tourist_destination_name)
#         img_base64_arr.append(img_base64)
#         price_arr.append(price)
#         the_right_time_to_go_arr.append(the_right_time_to_go)
#         tourist_destination_describe_arr.append(tourist_destination_describe)
#         tourist_destination_location_arr.append(tourist_destination_location)
#         number_of_stars_arr.append(number_of_stars)
#         number_of_travel_days_arr.append(number_of_travel_days)
#         type_file_arr.append(type_file_)

        
#     return {
#             "response":{
#                 "tourist_destination_name_arr":tourist_destination_name_arr,
#                 "img_base64_arr":img_base64_arr,
#                 "price_arr": price_arr,
#                 "the_right_time_to_go_arr":the_right_time_to_go_arr,
#                 "tourist_destination_describe_arr":tourist_destination_describe_arr,
#                 "tourist_destination_location_arr":tourist_destination_location_arr,
#                 "number_of_stars_arr":number_of_stars_arr,
#                 "number_of_travel_days_arr":number_of_travel_days_arr,
#                 "type_file_arr":type_file_arr
#             }
#         }