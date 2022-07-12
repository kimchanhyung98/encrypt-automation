from services.common import *
from services.email import *

for i in range(1, count_column()):
    origin_data = get_data(i)
    print('id: ', i, ', origin: ', origin_data)

    if origin_data is not None:
        processed_data = crypto(origin_data)
        update_data(processed_data, i)
