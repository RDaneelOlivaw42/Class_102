import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)

    #initializing cv2
    # cv2.VideoCapture(0) -> initiates use of primary camera - front camera
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        # takes a photo, saves data in (ret, frame) 
        # ret -> binary, saves wether photo has been taken or not
        # frame -> stores photo taken
        ret, frame = videoCaptureObject.read()

        img_name = "img_" + str(number) + ".png"

        # saves photo (var frame) taken with var img_name in current folder
        cv2.imwrite(img_name, frame)

        result = False
    
    return img_name
    print("Snapshot Taken")

    # stops camera running, and stops any other windows using camera as well
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = 'sl.BJxp_LUIrGrJ6xvaTys0sF4mOnt2SPQebbqZrdGweN3aFkNkX2LestQYbiAJWNTAxa9TzLYikL3OepVCLXHvP94d_4W2loKcR6ZPcn43RxlpqDHqkUCDgztswB9bchTI9gnteKNr_2A'
    file_from = img_name
    file_to = "/test_folder/" + (img_name)

    dbx = dropbox.Dropbox(access_token)

    # open(file_from, 'rb') - opens file in mode so as to be read in binary form
    # conjecture: possible reasoning, save processing power
    with open(file_from, 'rb') as f:

        # dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        # f.read -> means creates a copy of f (see line 46), to be read, and saves this copy to dropbox
        # file_to -> location on dropbox where file is saved (see line 40)
        # mode -> specifies how to handle situation if file to be uploaded has same name as a previously uploaded (existing) file
        # dropbox.files.WriteMode.overwrite -> overwrites existing file's data
        #                                   -> auto-rename strategy: append a number to the file name
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while(True):
        # if camera takes photo (current time - time when function was started) for more than or equal to 1 minute
        if((time.time() - start_time) >= 1):
            name = take_snapshot()
            # name -> var img_name
            upload_file(name)

main()