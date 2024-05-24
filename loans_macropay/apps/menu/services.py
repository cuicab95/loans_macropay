class MenuServices:

    @classmethod
    def build_menu_tree(cls, queryset, parent_id=None):
        result = []
        for menu in queryset:
            if menu.parent_id == parent_id:
                children = cls.build_menu_tree(queryset, menu.external_id)
                if menu.type_menu == "basic":
                    node = {
                        "id": menu.external_id,
                        "title": menu.title,
                        "type": menu.type_menu,
                        "icon": menu.icon,
                        "link": menu.link,
                    }
                elif menu.type_menu == "collapsable":
                    node = {
                        "title": menu.title,
                        "type": menu.type_menu,
                        "icon": menu.icon,
                    }
                else:
                    node = {
                        "title": menu.title,
                        "type": menu.type_menu,
                    }
                if children:
                    node['children'] = children
                result.append(node)
        return result