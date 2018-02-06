from base import *

data = {
    # body
    position: [0, 0],  # X, Y
    size: [1960, 1320],  # Width, Height
    background: [255, 255, 255],  # image / None / [R, G, B]
    children: [{
        # nav
        position: [0, 0],
        size: [1960, 56],
        background: [255, 255, 255],
        children: [{
            # left
            position: [24, 16],
            size: [24, 24],
            background: image,
        }, {
            # logo
            position: [72, 16],
            size: [88, 24],
            background: image,
        }, {
            # search-box
            position: [242, 13],
            size: [656, 32],
            children: [{
                # search-input
                position: [0, 0],
                size: [591, 32],
                background: [255, 255, 255],
                border: [[204, 204, 204], 1],  # [[R, G, B], Width]
                text: [[0, 0, 0], 16, "english"],  # [[R, G, B], FontSize, String]
                type_: input_,
                # end search-input
            }, {
                # search-btn
                position: [591, 0],
                size: [65, 32],
                background: [248, 248, 248],
                children: [{
                    # search-icon
                    position: [23, 6],
                    size: [20, 20],
                    background: image,
                    # end search-icon
                }],
                # search-btn
            }],
            # env search-box
        }, {
            # upload-btn
            position: [1748, 16],
            size: [24, 24],
            background: image,
            # end upload-btn
        }, {
            # menu-btn
            position: [1795, 16],
            size: [24, 24],
            background: image,
            # end menu-btn
        }, {
            # alert-btn
            position: [1843, 16],
            size: [24, 24],
            background: image,
            # end alert-btn
        }, {
            # avatar
            position: [1897, 13],
            size: [32, 32],
            background: image,
            border_radius: [16, 16],
            # end avatar
        }],
        # end nav
    }, {
        # main-container
        position: [127, 80],
        size: [1280, 1010],
        children: [{
            # video
            position: [0, 0],
            size: [1280, 720],
            background: image,
            # end video
        }, {
            # title
            position: [0, 740],
            size: [620, 28],
            text: [[0, 0, 0], 18, "Learn English in 3 Hours - ALL You Need to Master English Conversation"],
            # end title
        }, {
            # click-info
            position: [0, 768],
            size: [118, 19],
            text: [[17, 17, 17], 16, "1,481,538 views"],
            # end click-info
        }, {
            # right-menu
            position: [932, 778],
            size: [340, 20],
            children: [{
                # thumb-up
                position: [0, 0],
                size: [64, 20],
                children: [{
                    # thumb-up-btn
                    position: [0, 0],
                    size: [20, 20],
                    background: image,
                    # end thumb-up-btn
                }, {
                    # thumb-up-count
                    position: [28, 2],
                    size: [37, 15],
                    text: [[17, 17, 17], 13, "20000"],
                    # end thumb-up-count
                }],
                # end thumb-up
            }, {
                # thumb-down
                position: [89, 0],
                size: [50, 20],
                children: [{
                    # thumb-down-btn
                    position: [0, 0],
                    size: [20, 20],
                    background: image,
                    # end thumb-down-btn
                }, {
                    # thumb-down-count
                    position: [28, 2],
                    size: [23, 15],
                    text: [[17, 17, 17], 13, "888"],
                    # end thumb-down-count
                }],
                # end thumb-down
            }, {
                # share
                position: [162, 0],
                size: [84, 20],
                children: [{
                    # share-btn
                    position: [0, 0],
                    size: [20, 20],
                    background: image,
                    # end share-btn
                }, {
                    # share-text
                    position: [28, 2],
                    size: [60, 15],
                    text: [[17, 17, 17], 13, "SHARE IT"],
                    # end share-text
                }],
                # end-share
            }, {
                # subscribe-btn
                position: [272, 0],
                size: [20, 20],
                background: image,
                # end subscribe-btn
            }, {
                # more-btn
                position: [317, 0],
                size: [20, 20],
                background: image,
                # end more-btn
            }],
            # end right-menu
        }, {
            # producer
            position: [0, 832],
            size: [1260, 156],
            children: [{
                # avatar
                position: [0, 0],
                size: [48, 48],
                background: image,
                border_radius: [24, 24],
                # end avatar
            }, {
                # name
                position: [64, 9],
                size: [260, 16],
                text: [[0, 0, 0], 14, "Learn English with EnglishClass101.com"],
                # end name
            }, {
                # post-time
                position: [64, 28],
                size: [145, 15],
                text: [[17, 17, 17], 13, "Posted on April 11, 2017"],
                # end post-time
            }, {
                # content
                position: [64, 64],
                size: [600, 41],
                text: [[0, 0, 0], 13, "This 3 hours of English topics WILL make your English sound more natural! If you want to study "
                                      "more, click here: https://goo.gl/48uDNw and learn English in the most efficient way. More detai"],
                # end content
            }, {
                # subscribe-btn
                position: [1115, 8],
                size: [164, 36],
                background: [255, 0, 0],
                children: [{
                    # text
                    position: [16, 10],
                    size: [132, 16],
                    text: [[255, 255, 255], 13, "SUBSCRIBE 880,000"],
                    # end text
                }],
                # end subscribe-btn
            }],
            # end producer
        }],
        # end main-container
    }],
    # end body
}
