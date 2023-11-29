from django.test import TestCase
from django.urls import reverse
from apps.accounts.models import UserModel, GroupModel


class UserListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Створюємо користувачів: менеджерів і не-менеджерів
        number_of_users = 5
        for user_id in range(number_of_users):
            user = UserModel.objects.create(
                first_name=f'User {user_id}',
                last_name=f'Lastname {user_id}',
                email=f'user{user_id}@example.com',
                is_manager=(user_id % 2 == 0)  # Половина будуть менеджерами
            )
            user.set_password('12345')
            user.save()

        # Створення тестового користувача для авторизації
        cls.test_user = UserModel.objects.create(
            email='test@example.com',
            first_name='Test',
            last_name='User',
            is_manager=False
        )
        cls.test_user.set_password('12345')
        cls.test_user.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users_list.html')

    def test_lists_all_non_managers(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['users']), 3)

    def test_context_data(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.context['title'], 'List of users')
        self.assertEqual(response.context['button_label'], 'Create user')

    def test_view_with_authenticated_user(self):
        self.client.login(email='test@example.com', password='12345')
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_with_anonymous_user(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)


class CustomUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Створюємо звичайного користувача
        cls.user = UserModel.objects.create(
            email='user@example.com', first_name='User', last_name='Test'
        )
        cls.user.set_password('userpassword')
        cls.user.save()

        # Створюємо менеджера
        cls.manager = UserModel.objects.create(
            email='manager@example.com', first_name='Manager', last_name='Test', is_manager=True
        )
        cls.manager.set_password('managerpassword')
        cls.manager.save()

    def test_update_view_template_for_manager(self):
        self.client.login(email='manager@example.com', password='managerpassword')
        response = self.client.get(reverse('user-edit', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_user.html')

    def test_update_view_permission_for_regular_user(self):
        self.client.login(email='user@example.com', password='userpassword')
        response = self.client.get(reverse('user-edit', kwargs={'pk': self.manager.pk}))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('error'))

    def test_update_view_permission_for_unauthenticated_user(self):
        response = self.client.get(reverse('user-edit', kwargs={'pk': self.user.pk}))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('error'))


class CustomDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = UserModel.objects.create(
            email='user@example.com', first_name='User', last_name='Test'
        )
        cls.user.set_password('userpassword')
        cls.user.save()


        cls.manager = UserModel.objects.create(
            email='manager@example.com', first_name='Manager', last_name='Test', is_manager=True
        )
        cls.manager.set_password('managerpassword')
        cls.manager.save()

    def test_delete_view_template(self):
        self.client.login(email='manager@example.com', password='managerpassword')
        response = self.client.get(reverse('user-delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')

    def test_delete_view_permission_for_regular_user(self):
        self.client.login(email='user@example.com', password='userpassword')
        response = self.client.get(reverse('user-delete', kwargs={'pk': self.manager.pk}))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('error'))

    def test_delete_view_permission_for_unauthenticated_user(self):
        response = self.client.get(reverse('user-delete', kwargs={'pk': self.user.pk}))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('error'))

    def test_delete_action(self):
        self.client.login(email='manager@example.com', password='managerpassword')
        response = self.client.post(reverse('user-delete', kwargs={'pk': self.user.pk}))
        self.assertRedirects(response, reverse('user-list'))
        self.assertFalse(UserModel.objects.filter(pk=self.user.pk).exists())


class GroupListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Створення кількох тестових груп
        number_of_groups = 5
        for group_num in range(number_of_groups):
            GroupModel.objects.create(name=f'Group {group_num}', description=f'Description {group_num}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('group-list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('group-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'groups_list.html')

    def test_lists_all_groups(self):
        response = self.client.get(reverse('group-list'))
        self.assertEqual(response.status_code, 200)
        # Перевіряємо, що у контексті є 5 груп
        self.assertTrue(len(response.context['groups']) == 5)


class GroupCreateViewTest(TestCase):

    def test_create_view_template(self):
        response = self.client.get(reverse('group-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_group.html')

    def test_create_group_functionality(self):
        group_data = {
            'name': 'Group11',
            'description': 'Description111'
        }
        response = self.client.post(reverse('group-add'), group_data)
        self.assertRedirects(response, reverse('group-list'))
        self.assertTrue(GroupModel.objects.filter(name='Group11').exists())

    def test_create_view_context_data(self):
        response = self.client.get(reverse('group-add'))
        self.assertEqual(response.context['title'], 'Create group')
        self.assertEqual(response.context['button_label'], 'Create')

class GroupUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.manager = UserModel.objects.create(
                        email='manager@example.com', first_name='Manager', last_name='Test', is_manager=True
                    )
        cls.manager.set_password('managerpassword')
        cls.manager.save()

        cls.group = GroupModel.objects.create(name='Test Group', description='Test Description')

    def test_update_view_template_for_manager(self):
        self.client.login(email='manager@example.com', password='managerpassword')
        response = self.client.get(reverse('group-edit', kwargs={'pk': self.group.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_group.html')

    def test_update_group_functionality(self):
        self.client.login(email='manager@example.com', password='managerpassword')
        updated_data = {
            'name': 'Group11',
            'description': 'Description11'
        }
        response = self.client.post(reverse('group-edit', kwargs={'pk': self.group.pk}), updated_data)
        self.assertRedirects(response, reverse('group-list'))
        updated_group = GroupModel.objects.get(pk=self.group.pk)
        self.assertEqual(updated_group.name, 'Group11')
        self.assertEqual(updated_group.description, 'Description11')

    def test_update_view_permission_for_unauthorized_user(self):
        response = self.client.get(reverse('group-edit', kwargs={'pk': self.group.pk}))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('error'))

    def test_update_view_context_data(self):
        self.client.login(email='manager@example.com', password='managerpassword')
        response = self.client.get(reverse('group-edit', kwargs={'pk': self.group.pk}))
        self.assertEqual(response.context['title'], 'Edit group')
        self.assertEqual(response.context['button_label'], 'Save changes')
        self.assertTrue('users' in response.context)


# class GroupDeleteViewTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         # Створення користувача-менеджера
#         cls.manager = UserModel.objects.create(
#             email='manager@example.com', is_manager=True
#         )
#         cls.manager.set_password('managerpassword')
#         cls.manager.save()
#
#         cls.group_with_users = GroupModel.objects.create(name='Group with Users', description='Description')
#         cls.group_empty = GroupModel.objects.create(name='Empty Group', description='Description')
#
#         user = UserModel.objects.create(email='user@example.com')
#         user.set_password('userpassword')
#         user.save()
#         cls.group_with_users.users.add(user)
#
#     def test_delete_view_template_for_manager(self):
#         self.client.login(email='manager@example.com', password='managerpassword')
#         response = self.client.get(reverse('group-delete', kwargs={'pk': self.group_empty.pk}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'confirm_delete.html')
#
#     def test_delete_view_permission_for_unauthorized_user(self):
#         response = self.client.get(reverse('group-delete', kwargs={'pk': self.group_empty.pk}))
#         self.assertNotEqual(response.status_code, 200)
#         self.assertRedirects(response, reverse('error'))
#
#     def test_prevent_deletion_of_group_with_users(self):
#         self.client.login(email='manager@example.com', password='managerpassword')
#         response = self.client.post(reverse('group-delete', kwargs={'pk': self.group_with_users.pk}))
#         self.assertRedirects(response, reverse('group_list_page'))
#         self.assertTrue(GroupModel.objects.filter(pk=self.group_with_users.pk).exists())
#
#     def test_delete_empty_group(self):
#         self.client.login(email='manager@example.com', password='managerpassword')
#         response = self.client.post(reverse('group-delete', kwargs={'pk': self.group_empty.pk}))
#         self.assertRedirects(response, reverse('group-list'))
#         self.assertFalse(GroupModel.objects.filter(pk=self.group_empty.pk).exists())