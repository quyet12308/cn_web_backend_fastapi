# Vấn đề 1 : 1 email có thể có nhiều user

# vấn đề 2 : lỗi logic khi cố xóa code catcha trực tiếp -> hướng giải quyết : truyền thêm 1 trường time vào và so sánh với time hiện tại (lớn hơn 3 phút thì ko nhận ) . Có thể giải quyết để nâng cấp qua các hướng như : tự động xóa , database triggers , lập lịch (scheduler) 