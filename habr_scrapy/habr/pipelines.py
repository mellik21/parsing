
class HabrPipeline(object):
    @classmethod
    def process_item(self, item, spider):
        item['title'] = item['title']
        item['author'] = item['author']
        return item
