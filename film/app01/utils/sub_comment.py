from app01.models import CommentSharing


def find_root_sub_comment(root_comment, sub_comment_list):
    for sub_comment in root_comment.commentsharing_set.all():
        sub_comment_list.append(sub_comment)
        find_root_sub_comment(sub_comment, sub_comment_list)


def sub_comment_list(nid):
    comment_query = CommentSharing.objects.filter(sharing_id=nid).order_by('-create_date')

    comment_list = []
    for comment in comment_query:
        if not comment.parent_comment:
            # 查找根评论下的所有子评论
            lis = []
            find_root_sub_comment(comment, lis)
            comment.sub_comment = lis
            comment_list.append(comment)
            continue
    return comment_list
