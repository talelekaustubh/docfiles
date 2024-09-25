import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.core.Application;
import javax.ws.rs.core.Response;
import java.util.HashSet;
import java.util.Set;

@Path("/")
public class App extends Application {

    @GET
    public Response hello() {
        return Response.ok("Hello from Krishna With Java in Docker!").build();
    }

    public Set<Class<?>> getClasses() {
        Set<Class<?>> classes = new HashSet<>();
        classes.add(App.class);
        return classes;
    }
}