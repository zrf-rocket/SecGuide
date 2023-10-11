未对输入和输出做过滤，场景：
```python
def xss_test(request):
    name = request.GET['name']
    return HttpResponse('hello %s' %(name))
```
在代码中一搜，发现有大量地方使用，比较正确的使用方式如下：
```python
def xss_test(request):
    name = request.GET['name']
    #return HttpResponse('hello %s' %(name))
    return render_to_response('hello.html', {'name':name})
```
更好的就是对输入做限制，比如说一个正则范围，输出使用正确的api或者做好过滤。 
